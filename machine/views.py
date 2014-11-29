__author__ = 'nikaashpuri'
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.views.generic.list import ListView
from django.utils import timezone
import time

from machine.models import Controller
from django.views.decorators.csrf import csrf_exempt
# import receiver

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


def collect_data_from_device_using_tcp(input_data):

    # binary_equivalent = ''.join(format(ord(i), 'b').zfill(8) for i in input_data)
    # print input_data
    # print 'In views file: ', input_data
    import receiver
    print 'calling receiver now...'
    receiver.ConvertAndSave(Controller, input_data)


def activate_server(request):

    # begin the TCP server
    import subprocess
    tcpip_server_file_path = '/Users/nikaashpuri/Documents/alibi_projects/aquabrim_project/machine/tcp_ip_server.py'
    # tcpip_server_file_path = '/public_html/aquabrim_project/machine/tcp_ip_server.py'
    subprocess.Popen(["python", tcpip_server_file_path])
    return HttpResponse('server has been started')


def commandData(request, data_id):

    return render_to_response('commands.html',
                              {'controller': Controller.objects.get(id=data_id)})


def submitData(request, data_id):

    controller = Controller.objects.get(id=data_id)

    command_id = int(request.GET.get('id'))

    idno = controller.device_id
    first_byte = convert2bin(idno[:3], 2)
    second_byte = convert2bin(idno[3:6], 2)
    third_byte = convert2bin(idno[6:], 8)
    idno = first_byte + second_byte + third_byte

    # id_bytes = convert2bin(idno, 24)
    command_byte = convert2bin(command_id, 8)

    PayloadA = "00000000"
    PayloadB = "00000000"

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

        PayloadA = convert2bin(sub_ID,6)+convert2bin(overflow_status,1)+convert2bin(flow_status,1)
        PayloadB = "0" + convert2bin(water_level, 7)


    elif(command_id==2):
        print "Empty for now!"
        PayloadA = ""
        PayloadB = ""


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

        PayloadA = convert2bin(sub_ID, 6) + convert2bin(full_level_alarm, 1) + convert2bin(low_level_alarm, 1)
        PayloadB = convert2bin(motor_trigger, 1) + convert2bin(flow_protection, 1) + convert2bin(enable_disable, 1) + convert2bin(no_signal_duration, 5)

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

        PayloadA = "00000000"
        PayloadB = convert2bin(trial_enabled, 1) + convert2bin(trial_period, 4) + convert2bin(timer_based, 1) + convert2bin(mode_selection, 2)


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

        PayloadA = convert2bin(Tx_type, 2) + convert2bin(water_level_type, 2) + convert2bin(offset_level_reset, 4)
        PayloadB = convert2bin(water_level, 8)


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

        PayloadA = convert2bin(restart_delay, 3) + "0" + convert2bin(trial_gap, 4)
        PayloadB = convert2bin(trial_duration, 4) + convert2bin(trials, 2) + convert2bin(operating_mn, 2)


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

        PayloadA = "000" + convert2bin(initial_start_delay, 4) + convert2bin(timeout_protection, 1)
        PayloadB = convert2bin(timeout_duration, 8)


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

        PayloadA = convert2bin(voltage_enable, 1) + convert2bin(offset_voltage, 4) + convert2bin(low_volt_protection, 1)
        Lv = convert2bin(low_voltage_point, 4)
        PayloadA = PayloadA + Lv[0:2]
        PayloadB = Lv[2:4] + convert2bin(high_volt_protection, 1) + convert2bin(high_voltage_point, 5)


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
        m = request.GET.get('m')
        if(not m==""):
            controller.m = m


        PayloadA = convert2bin(week_days, 3) + convert2bin(hours, 5)
        PayloadB = convert2bin(timer_enable, 1) + convert2bin(timer_number, 3) + convert2bin(m, 4)


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

        PayloadA = convert2bin(week_days, 3) + convert2bin(hours, 5)
        PayloadB = "00" + convert2bin(m, 6)


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

        PayloadA = "0000000" + convert2bin(no_signal_alarm_sump, 1)
        PayloadB = convert2bin(no_signal_alarm_top, 1) + convert2bin(manual_motor_on_alarm, 1) + convert2bin(motor_on_alarm, 1) + convert2bin(flow_error_alarm, 1) +convert2bin(timeout_alarm, 1) + convert2bin(high_voltage_alarm, 1) + convert2bin(low_voltage_alarm, 1) + convert2bin(Tx_alarm, 1)


    '''elif(command_id==12):
        pass


    elif(command_id==13):
        pass'''


    data_stream = idno + command_byte + PayloadA + PayloadB

    send_string(data_stream)

    controller.save()

    url = '/machine/get/%s/command' % data_id
    return HttpResponseRedirect(url)


def send_string(controller_data_to_send):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (TCP_SERVER_IP, TCP_SERVER_PORT)
    sock.connect(server_address)

    try:
        message = 'send ' + controller_data_to_send
        sock.sendall(message)

    finally:
        sock.close()


def convert2bin(val, length):
    try:
        a = bin(val)
    except TypeError:
        val = int(val)
        a = bin(val)
    a = a[2:]
    l = len(a)
    a = str(a)
    s = ""
    if (length-l>0):
        for i in range(0, (length-l)):
            s = s + "0"
        return (s+a)
    else:
        return a


def convert_bin_to_char(bin_text):
    return unichr(int(bin_text, 2))
