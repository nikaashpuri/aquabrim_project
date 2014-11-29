from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.views.generic.list import ListView
from django.utils import timezone
import time

from machine.models import Controller,Transmitter
from django.views.decorators.csrf import csrf_exempt

#changes made by shubham
#from machine.forms import DeviceForm
from django.conf.urls import patterns, include, url

import sys
import socket
import datetime


def list_change(request):
    on = int(request.GET.get('onoff',0))
    idno = request.GET.get('idno',1)
    controller = Controller.objects.get(id=idno)
    controller.onoff=on
    if on == 1:
        controller.onStatus = "On"
    else:
        controller.onStatus = "off"
    controller.save()
    return HttpResponseRedirect('/machine/')


class ControllerListView(ListView):

    model = Controller


    def get_context_data(self, **kwargs):
        context = super(ControllerListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        """Override get_querset so we can filter on request.user """
        return Controller.objects.filter(user=self.request.user)


def changeViews(request, data_id):
    '''
    This function is called whenever some change is made on any dial in the
    detailed settings page, so we need to collect the data that we
    want to send and then send it to the motor
    '''
    voltage = request.GET.get('voltage', 0)
    timeout = request.GET.get('timeout', 0)
    onoff = request.GET.get('on_off',0)
    hold = request.GET.get('hold', 0)
    vc = request.GET.get('vc', 0)
    tmout = request.GET.get('to', 0)

    # prepare dict to send
    dict_controller_field_to_value = {}
    dict_controller_field_to_value['voltage'] = int(voltage)
    dict_controller_field_to_value['timeout'] = int(timeout)
    dict_controller_field_to_value['on_or_off'] = int(onoff)
    dict_controller_field_to_value['hold'] = int(hold)
    dict_controller_field_to_value['voltage_control'] = int(vc)
    dict_controller_field_to_value['timeout_control'] = int(tmout)
    print dict_controller_field_to_value

    # ---------- send changes to device

    # ---------- assume we have got confirmation of changes

    controller = Controller.objects.get(id=data_id)
    controller.voltage = dict_controller_field_to_value['voltage']
    controller.timeout_interval = dict_controller_field_to_value['timeout']
    onoff = dict_controller_field_to_value['on_or_off']
    controller.onoff = onoff
    controller.hold = dict_controller_field_to_value['hold']
    controller.voltage_status = dict_controller_field_to_value['voltage_control']
    controller.timeout_status = dict_controller_field_to_value['timeout_control']

    '''
    if(onoff==1):
        controller.onStatus = "On"
    else:
        controller.onStatus = "off"
    '''
    controller.save()

    return render_to_response('index2.html',
                        {'data': controller})


def deviceData(request, data_id=1):

    return render_to_response('index2.html',
                        {'data': Controller.objects.get(id=data_id)})


import os
from aquabrim_project.settings import BASE_DIR


DATA_STORAGE_FOLDER = os.path.join(BASE_DIR, 'uploaded_files_from_board')
DATA_STORAGE_FILENAME = os.path.join(DATA_STORAGE_FOLDER, 'data_dump')
TCP_SERVER_IP = 'localhost'
TCP_SERVER_PORT = 40000


def update_controller_data(data):
    controller_object = Controller.objects.get(device_id = data['device_id'])

    if data['timestamp'] != 'NA':
        controller_object.timestamp = data['timestamp']
    if data['motor_status'] != 'NA':
        controller_object.motor_status = data['motor_status']
    if data['signal_status'] != 'NA':
        controller_object.signal_status = data['signal_status']
    if data['voltage'] != 'NA':
        controller_object.voltage = data['voltage']
    if data['ip_address'] != 'NA':
        controller_object.ip_address = data['ip_address']
    if data['machine_status'] != 'NA':
        controller_object.machine_status = data['machine_status']

    controller_object.save()


def update_transmitter_data(data):
    transmitter_object = Transmitter.objects.get(device_id = data['device_id'])

    if data['timestamp'] != 'NA':
        transmitter_object.timestamp = data['timestamp']
    if data['sub_id'] != 'NA':
        transmitter_object.sub_id = data['sub_id']
    if data['flow_status'] != 'NA':
        transmitter_object.flow_status = data['flow_status']
    if data['tank_75_full'] != 'NA':
        transmitter_object.tank_75_full = data['tank_75_full']
    if data['tank_50_full'] != 'NA':
        transmitter_object.tank_50_full = data['tank_50_full']
    if data['tank_25_full'] != 'NA':
        transmitter_object.tank_25_full = data['tank_25_full']
    if data['ip_address'] != 'NA':
        transmitter_object.ip_address = data['ip_address']

    transmitter_object.save()




def collect_data_from_device_using_tcp(input_data):

    binary_equivalent = ''.join(format(ord(i), 'b').zfill(8) for i in input_data)
    print input_data
    print binary_equivalent
    


def parse_incoming_data_using_tcp(data):

    ip_address = 'NA'

    # note using NA to denote empty value
    result_dict = {
        'device_id': '123457',
        'sub_id': 'NA',
        'tank_75_full': 'NA',
        'tank_50_full': 'NA',
        'tank_25_full': 'TRUE',
        'flow_status': 'NA',
        'timestamp': datetime.datetime.now(),
        'ip_address': ip_address,
        'motor_status': 'NA',
        'signal_status': 'NA',
        'voltage': '250',
        'name': 'NA',
        'controller_or_transmitter': 'C',
        'timeout_interval': 'NA',
        'machine_status': 'NA',
    }

    return result_dict


def activate_server(request):

    # begin the TCP server
    import subprocess
    # tcpip_server_file_path = os.path.join(BASE_DIR, 'machine', 'tcp_ip_server.py')
    tcpip_server_file_path = '/public_html/aquabrim_project/machine/tcp_ip_server.py'
    subprocess.Popen(["python", tcpip_server_file_path])
    return HttpResponse('')

def commandData(request, data_id):

    return render_to_response('commands.html',
                              {'controller': Controller.objects.get(id=data_id)})

def submitData(request, data_id):

    controller = Controller.objects.get(id=data_id)

    command_id = int(request.GET.get('id'))


    if(command_id==1):
        overflow_status = request.GET.get('overflow')
        if(not overflow_status==""):
            controller.overflow_status = overflow_status
        sub_ID = request.GET.get('sub_id')
        if(not sub_ID==""):
            controller.sub_ID = sub_ID
        flow_status = request.GET.get('flow_status')
        if(not flow_status==""):
            controller.flow_status = flow_status
        water_level = request.GET.get('water')
        if(not water_level==""):
            controller.water_level = water_level


    elif(command_id==2):
        print "Empty for now!"


    elif(command_id==3):
        sub_ID = request.GET.get('sub_id')
        if(not sub_ID==""):
            controller.sub_ID = sub_ID

        low_level_alarm = request.GET.get('lla')
        if(not low_level_alarm==""):
            controller.low_level_alarm = low_level_alarm
        full_level_alarm = request.GET.get('fla')
        if(not full_level_alarm==""):
            controller.full_level_alarm = full_level_alarm

        enable_disable = request.GET.get('End')
        if(not enable_disable==""):
            controller.enable_disable = enable_disable
        flow_protection = request.GET.get('fp')
        if(not flow_protection==""):
            controller.flow_protection = flow_protection
        motor_trigger = request.GET.get('mt')
        if(not motor_trigger==""):
            controller.motor_trigger = motor_trigger
        no_signal_duration = request.GET.get('nsd')
        if(not no_signal_duration==""):
            controller.no_signal_duration = no_signal_duration


    elif(command_id==4):
        mode_selection = request.GET.get('mode')
        if(not mode_selection==""):
            controller.mode_selection = mode_selection
        trial_period = request.GET.get('D')
        if(not trial_period==""):
            controller.trial_period = trial_period
        timer_based = request.GET.get('T')
        if(not timer_based==""):
            controller.timer_based = timer_based
        trial_enabled = request.GET.get('Tr')
        if(not trial_enabled==""):
            controller.trial_enabled = trial_enabled


    elif(command_id==5):
        print "HEY"
        Tx_type = request.GET.get('tx_type')
        if(not Tx_type==""):
            print "HELLO"
            controller.Tx_type = Tx_type

        offset_level_reset = request.GET.get('offset')
        if(not offset_level_reset==""):
            controller.offset_level_reset = offset_level_reset
        water_level_type = request.GET.get('water_type')
        if(not water_level_type==""):
            controller.water_level_type = water_level_type
        water_level = request.GET.get('water')
        if(not water_level==""):
            controller.water_level = water_level


    elif(command_id==6):
        operating_mn = request.GET.get('om')
        if(not operating_mn==""):
            controller.operating_mn = operating_mn
        trials = request.GET.get('n')
        if(not trials==""):
            controller.trials = trials
        trial_duration = request.GET.get('td')
        if(not trial_duration==""):
            controller.trial_duration = trial_duration
        trial_gap = request.GET.get('tg')
        if(not trial_gap==""):
            controller.trial_gap = trial_gap
        restart_delay = request.GET.get('rd')
        if(not restart_delay==""):
            controller.restart_delay = restart_delay


    elif(command_id==7):
        timeout_duration = request.GET.get('td')
        if(not timeout_duration==""):
            controller.timeout_duration = timeout_duration
        timeout_protection = request.GET.get('ep')
        if(not timeout_protection==""):
            controller.timeout_protection = timeout_protection
        initial_start_delay = request.GET.get('sd')
        if(not initial_start_delay==""):
            controller.initial_start_delay = initial_start_delay


    elif(command_id==8):
        voltage_enable = request.GET.get('en')
        if(not voltage_enable==""):
            controller.voltage_enable = voltage_enable

        high_voltage_point = request.GET.get('high')
        if(not high_voltage_point==""):
            controller.high_voltage_point = high_voltage_point
        low_voltage_point = request.GET.get('low')
        if(not low_voltage_point==""):
            controller.low_voltage_point = low_voltage_point
        offset_voltage = request.GET.get('ov')
        if(not offset_voltage==""):
            controller.offset_voltage = offset_voltage
        high_volt_protection = request.GET.get('hvp')
        if(not high_volt_protection==""):
            controller.high_volt_protection = high_volt_protection
        low_volt_protection = request.GET.get('lvp')
        if(not low_volt_protection==""):
            controller.low_volt_protection = low_volt_protection


    elif(command_id==9):
        timer_enable = request.GET.get('te')
        if(not timer_enable==""):
            controller.timer_enable = timer_enable
        week_days = request.GET.get('wd')
        if(not week_days==""):
            controller.week_days = week_days
        timer_number = request.GET.get('tn')
        if(not timer_number==""):
            controller.timer_number = timer_number
        hours = request.GET.get('h')
        if(not hours==""):
            controller.hours = hours


    elif(command_id==10):
        week_days = request.GET.get('wd')
        if(not week_days==""):
            controller.week_days = week_days
        hours = request.GET.get('h')
        if(not hours==""):
            controller.hours = hours
        m = request.GET.get('m')
        if(not m==""):
            controller.m = m


    elif(command_id==11):
        Tx_alarm = request.GET.get('Tx')
        if(not Tx_alarm==""):
            controller.Tx_alarm = Tx_alarm
        low_voltage_alarm = request.GET.get('lva')
        if(not low_voltage_alarm==""):
            controller.low_voltage_alarm = low_voltage_alarm
        high_voltage_alarm = request.GET.get('hva')
        if(not high_voltage_alarm==""):
            controller.high_voltage_alarm = high_voltage_alarm
        timeout_alarm = request.GET.get('toa')
        if(not timeout_alarm==""):
            controller.timeout_alarm = timeout_alarm
        flow_error_alarm = request.GET.get('fe')
        if(not flow_error_alarm==""):
            controller.flow_error_alarm = flow_error_alarm
        motor_on_alarm = request.GET.get('mo')
        if(not motor_on_alarm==""):
            controller.motor_on_alarm = motor_on_alarm
        manual_motor_on_alarm = request.GET.get('mmo')
        if(not manual_motor_on_alarm==""):
            controller.manual_motor_on_alarm = manual_motor_on_alarm
        no_signal_alarm_top = request.GET.get('nsat')
        if(not no_signal_alarm_top==""):
            controller.no_signal_alarm_top = no_signal_alarm_top
        no_signal_alarm_sump = request.GET.get('nsas')
        if(not no_signal_alarm_sump==""):
            controller.no_signal_alarm_sump = no_signal_alarm_sump


    '''elif(command_id==12):
        pass


    elif(command_id==13):
        pass'''




    controller.save()

    url = '/machine/get/%s/command' % data_id
    return HttpResponseRedirect(url)
#defining functions for the conversion of the data to binary stream to be set to the transmitter through a function for each of the commands!


#def one(device_id, sub_id, flow_status, overflow_status, water_level):

def send_string_to_start_motor(request):
    """
    the controller will send a string to activate a command at the receiver
    the following functionalities must be expressed:
    state of the machine - ON / OFF / HOLD
    voltage - value of voltage / DISABLED
    timeout_interval - value / DISABLED

    string structure
    <state> <voltage> <timeout>
    """

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('162.251.84.104', 40000)
    sock.connect(server_address)

    try:
        message = 'send +CSTS1'
        sock.sendall(message)

    finally:
        sock.close()

    # return HttpResponse('you have started your motor')
    return render_to_response('stop_motor.html',
                        {})


def send_string_to_stop_motor(request):

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('162.251.84.104', 40000)
    sock.connect(server_address)

    try:
        message = 'send +CSTS0'
        sock.sendall(message)

    finally:
        sock.close()

    # return HttpResponse('you have stopped your motor')
    return render_to_response('start_motor.html',
                        {})


def send_string(controller_data_to_send):
    """
    the controller will send a string to activate a command at the receiver
    the following functionalities must be expressed:
    state of the machine - ON / OFF / HOLD
    voltage - value of voltage / DISABLED
    timeout_interval - value / DISABLED

    string structure
    <state> <voltage> <timeout>
    """

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (TCP_SERVER_IP, TCP_SERVER_PORT)
    sock.connect(server_address)

    try:
        message = 'send +CSTS1'
        sock.sendall(message)

    finally:
        sock.close()

    # return HttpResponse('you have started your motor')
    return render_to_response('stop_motor.html',
                        {})
