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
import file_locations_and_constants
from django.utils.timezone import now
from datetime import timedelta
from models import Timer, Tank

def list_change(request):
    on = int(request.GET.get('onoff', 0))
    idno = request.GET.get('idno', 1)
    controller = Controller.objects.get(id=idno)
    controller.onoff = on
    if on == 1:
        controller.onStatus = "On"
        Controller.objects.all().filter(device_id=controller.device_id).update(onStatus="On")
    else:
        controller.onStatus = "off"
        Controller.objects.all().filter(device_id=controller.device_id).update(onStatus="off")

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
    onoff = request.GET.get('on_off', 0)
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
    return HttpResponseRedirect('user_interface')


def userInterface(request, data_id=1):
    controller = Controller.objects.get(id=data_id)
    list_of_tanks = Tank.objects.all().filter(controller=controller, display=1)
    # print list_of_tanks
    tank_to_focus_on = int(request.GET.get('tank_to_focus_on', 0))
    # controller = list_of_tanks[tank_to_focus_on]

    if controller.graphical_or_not == 1:
        return render_to_response('tank.html',
                              {'data': list_of_tanks[tank_to_focus_on],
                               'list_of_tanks': list_of_tanks,
                               'tank_to_focus_on': tank_to_focus_on,
                               'controller': controller})
    else:
        return render_to_response('index.html',
                              {'controller': controller,
                               'list_of_tanks': list_of_tanks,
                               })

def userInterfaceControllerSetting(request, data_id=1):
    return render_to_response('controller-setting.html',
                              {'data': Controller.objects.get(id=data_id)})

def userInterfaceDisplaySetting(request, data_id=1):
    return render_to_response('display-setting.html',
                              {'data': Controller.objects.get(id=data_id)})

def userInterfaceTankSetting(request, data_id=1):
    controller = Controller.objects.get(id=data_id)
    list_of_tanks = Tank.objects.all().filter(controller=controller)
    # print list_of_tanks

    return render_to_response('tank-setting.html',
                              {'list_of_tanks':list_of_tanks})

def userInterfaceTimerSetting(request, data_id=1):
    controller_object = Controller.objects.get(id=data_id)
    list_timers = Timer.objects.all().filter(controller=controller_object)

    return render_to_response('timer-setting.html',
                              {'data': controller_object,
                               'list_timers': list_timers})

import os
from aquabrim_project.settings import BASE_DIR


DATA_STORAGE_FOLDER = os.path.join(BASE_DIR, 'uploaded_files_from_board')
DATA_STORAGE_FILENAME = os.path.join(DATA_STORAGE_FOLDER, 'data_dump')
TCP_SERVER_IP = file_locations_and_constants.TCP_SERVER_IP
TCP_SERVER_PORT = file_locations_and_constants.TCP_SERVER_PORT


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

    tcpip_server_file_path = file_locations_and_constants.TCP_SERVER_FILE_PATH

    subprocess.Popen(["python", tcpip_server_file_path])
    return HttpResponse('server has been started')


def masterCommandData(request, data_id):
    aux_controller = Controller.objects.get(id=data_id)
    if aux_controller.com_last_access_auth_or_not == 0:
        aux_controller.com_last_access_auth_or_not = 1
        aux_controller.save()
        return render_to_response('master_commands_minimal.html',
                              {'data': aux_controller,
                               'auth': 0})
    else:
        return render_to_response('master_commands_minimal.html',
                              {'data': aux_controller})



def masterSubmitData(request, data_id):

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

    password = request.GET.get('pass')
    m = request.GET.get('m')
    t = request.GET.get('t')
    tr = request.GET.get('tr')
    d = request.GET.get('d')

    print request.GET


    if controller.com_pass == password:
        controller.com_m = m
        controller.com_t = t
        controller.com_tr = tr
        controller.com_d = d

        d = int(d)/2

        PayloadA = password
        PayloadB = convert2bin(tr, 1) + convert2bin(d, 4) \
                   + convert2bin(t, 1) \
                   + convert2bin(m, 2)
    else:
        controller.com_last_access_auth_or_not = 0



    data_stream = idno + command_byte + PayloadA + PayloadB
    # print data_stream
    send_string(data_stream)

    controller.save()


    url = '/machine/get/%s/master_command' % data_id
    return HttpResponseRedirect(url)




def commandData(request, data_id):
    aux_controller = Controller.objects.get(id=data_id)
    list_of_tanks = Tank.objects.all().filter(controller=aux_controller)
    return render_to_response('commands_minimal.html',
                              {'list_of_tanks': list_of_tanks,
                               'data': aux_controller})



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

    print request.GET

    if (command_id == 3):
        sub_ID = request.GET.get('sub_id', controller.sub_ID)
        tank = Tank.objects.get(controller=controller, sub_ID=sub_ID)

        low_level_alarm = tank.low_level_alarm
        full_level_alarm = tank.full_level_alarm

        enable_disable = request.GET.get('End')
        controller.enable_disable = enable_disable

        flow_protection = request.GET.get('fp')
        controller.flow_protection = flow_protection

        motor_trigger = tank.motor_trigger

        no_signal_duration = request.GET.get('nsd')
        controller.no_signal_duration = no_signal_duration

        tank.save()

        PayloadA = convert2bin(sub_ID, 6) + convert2bin(full_level_alarm, 1) + convert2bin(low_level_alarm, 1)
        PayloadB = convert2bin(motor_trigger, 1) + \
                   convert2bin(flow_protection, 1) + \
                   convert2bin(enable_disable, 1) + \
                   convert2bin(no_signal_duration, 5)


    elif (command_id == 5):

        Tx_type = request.GET.get('tx_type')
        controller.Tx_type = Tx_type

        sub_ID = request.GET.get('sub_id')
        tank = Tank.objects.get(controller=controller, sub_ID=sub_ID)


        offset_level_reset = request.GET.get('offset')
        tank.offset_level_reset = offset_level_reset

        water_level_type = request.GET.get('water_level_type')
        if int(water_level_type) == 1:
            water_level = tank.full_water_level
        else:
            water_level = tank.low_water_level

        tank.save()

        offset_level_reset = int(offset_level_reset)
        offset_level_reset = (offset_level_reset - 10) / 5

        PayloadA = convert2bin(sub_ID, 6) + convert2bin(offset_level_reset, 2)
        PayloadB = convert2bin(water_level_type, 1) + convert2bin(water_level, 7)



    data_stream = idno + command_byte + PayloadA + PayloadB
    # print data_stream
    send_string(data_stream)

    controller.save()

    url = '/machine/get/%s/command' % data_id
    return HttpResponseRedirect(url)


def submitDataUIHome(request, data_id):
    submitDataFromUserInterface(request, data_id)
    url = '/machine/get/%s' % data_id
    return HttpResponseRedirect(url)

def submitDataUIController(request, data_id):
    submitDataFromUserInterface(request, data_id)
    url = '/machine/get/%s/user_interface/controller-setting' % data_id
    return HttpResponseRedirect(url)


def submitDataUITank(request, data_id):
    submitDataFromUserInterface(request, data_id)
    url = '/machine/get/%s/user_interface/tank-setting' % data_id
    return HttpResponseRedirect(url)


def submitDataUITimer(request, data_id):
    submitDataFromUserInterface(request, data_id)
    url = '/machine/get/%s/user_interface/timer-setting' % data_id
    return HttpResponseRedirect(url)

def submitDataUIDisplay(request, data_id):
    submitDataFromUserInterface(request, data_id)
    url = '/machine/get/%s/user_interface/display-setting' % data_id
    return HttpResponseRedirect(url)

def submitDataFromUserInterface(request, data_id):


    controller = Controller.objects.get(id=data_id)

    controller.last_update = now() + timedelta(hours=5.5)

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

    print request.GET

    if (command_id == 3):
        sub_ID = request.GET.get('sub_id')
        tank = Tank.objects.get(controller=controller, sub_ID=sub_ID)


        low_level_alarm = request.GET.get('lla', 0)
        tank.low_level_alarm = low_level_alarm

        full_level_alarm = request.GET.get('fla', 0)
        tank.full_level_alarm = full_level_alarm

        overflow_alarm = request.GET.get('ofa', 0)
        tank.overflow_alarm = overflow_alarm

        flow_protection = request.GET.get('fp',
                                          0)
        controller.flow_protection = flow_protection

        motor_trigger = request.GET.get('mt', 0)
        tank.motor_trigger = motor_trigger

        no_signal_duration = request.GET.get('nsd', controller.no_signal_duration)


        PayloadA = convert2bin(sub_ID, 6) + convert2bin(full_level_alarm, 1) + convert2bin(low_level_alarm, 1)
        PayloadB = convert2bin(motor_trigger, 1) + \
                   convert2bin(flow_protection, 1) + \
                   "1" + \
                   convert2bin(no_signal_duration, 5)



        display = request.GET.get('dsp', 0)
        tank.display = display

        motor_trigger = request.GET.get('tm', 0)
        tank.motor_trigger = motor_trigger

        tank.save()


    elif (command_id == 4):
        mode_selection = request.GET.get('mode')
        if (not mode_selection == ""):
            controller.mode_selection = mode_selection
        trial_period = request.GET.get('D')
        if (not trial_period == ""):
            controller.trial_period = trial_period
        timer_based = request.GET.get('T')
        if (not timer_based == ""):
            controller.timer_based = timer_based
        trial_enabled = request.GET.get('Tr')
        if (not trial_enabled == ""):
            controller.trial_enabled = trial_enabled

        PayloadA = "00000000"
        PayloadB = convert2bin(trial_enabled, 1) + convert2bin(trial_period, 4) + convert2bin(timer_based,
                                                                                              1) + convert2bin(
            mode_selection, 2)


    elif (command_id == 5):

        sub_ID = request.GET.get('sub_id')
        tank = Tank.objects.get(controller=controller, sub_ID=sub_ID)

        Tx_type = request.GET.get('tx_type', controller.Tx_type)
        controller.Tx_type = Tx_type

        offset_level_reset = request.GET.get('offset', tank.offset_level_reset)
        tank.offset_level_reset = offset_level_reset

        water_level_type = request.GET.get('water_type', tank.water_level_type)
        tank.water_level_type = water_level_type


        if int(water_level_type) == 1:
            full_water_level = request.GET.get('water')
            tank.full_water_level = full_water_level
            water_level = tank.full_water_level
        elif int(water_level_type) == 0:
            low_water_level = request.GET.get('water')
            tank.low_water_level = low_water_level
            water_level = tank.low_water_level
        else:
            water_level = tank.water_level

        tank.save()

        offset_level_reset = int(offset_level_reset)
        offset_level_reset = (offset_level_reset - 10) / 5

        PayloadA = convert2bin(sub_ID, 6) + convert2bin(offset_level_reset, 2)
        PayloadB = convert2bin(water_level_type, 1) + convert2bin(water_level, 7)


    elif (command_id == 6):

        operating_mn = request.GET.get('om', controller.operating_mn)
        controller.operating_mn = operating_mn

        trials = request.GET.get('n', controller.trials)
        controller.trials = trials

        trial_duration = request.GET.get('td', controller.trial_duration)
        controller.trial_duration = trial_duration

        trial_gap = request.GET.get('tg', controller.trial_gap)
        controller.trial_gap = trial_gap

        restart_delay = request.GET.get('rd', controller.restart_delay)
        controller.restart_delay = restart_delay

        trial_duration = int(trial_duration) / 2
        trial_gap = int(trial_gap) / 3

        PayloadA = convert2bin(restart_delay, 3) + convert2bin(trial_duration, 5)
        PayloadB = convert2bin(trial_gap, 4) + convert2bin(trials, 2) + convert2bin(operating_mn, 2)


    elif (command_id == 7):

        timeout_duration = request.GET.get('td', controller.timeout_duration)
        controller.timeout_duration = timeout_duration


        if request.GET.has_key('ri') or request.GET.has_key('sd'):
            timeout_protection = controller.timeout_protection
        else:
            timeout_protection = request.GET.get('ep', 0)
            controller.timeout_protection = timeout_protection

        initial_start_delay = request.GET.get('sd', controller.initial_start_delay)
        controller.initial_start_delay = initial_start_delay

        reset_interval = request.GET.get('ri', controller.reset_interval)
        controller.reset_interval = reset_interval


        reset_interval = int(reset_interval) / 15
        timeout_duration = int(timeout_duration)
        timeout_duration = (timeout_duration - 60) / 2

        PayloadA = convert2bin(reset_interval, 3) + convert2bin(initial_start_delay, 4) + convert2bin(timeout_protection, 1)
        PayloadB = convert2bin(timeout_duration, 8)


    elif (command_id == 8):

        voltage_enable = request.GET.get('en', controller.voltage_enable)
        controller.voltage_enable = voltage_enable

        high_voltage_point = request.GET.get('high', controller.high_voltage_point)
        controller.high_voltage_point = high_voltage_point

        low_voltage_point = request.GET.get('low', controller.low_voltage_point)
        controller.low_voltage_point = low_voltage_point

        offset_voltage = request.GET.get('ov', controller.offset_voltage)
        controller.offset_voltage = offset_voltage

        if not request.GET.has_key('high'):
            high_volt_protection = controller.high_volt_protection
        elif not request.GET.has_key('hvp'):
            high_volt_protection = 0
        else:
            high_volt_protection = request.GET.get('hvp')

        controller.high_volt_protection = high_volt_protection

        if not request.GET.has_key('low'):
            low_volt_protection = controller.low_volt_protection
        elif not request.GET.has_key('lvp'):
            low_volt_protection = 0
        else:
            low_volt_protection = request.GET.get('lvp')

        controller.low_volt_protection = low_volt_protection

        high_voltage_point = int(high_voltage_point)
        low_voltage_point = int(low_voltage_point)

        high_voltage_point = (high_voltage_point - 240) / 4
        low_voltage_point = (200 - low_voltage_point) / 3

        PayloadA = convert2bin(offset_voltage, 4) + convert2bin(low_voltage_point, 4)
        PayloadB = "0" + convert2bin(low_volt_protection, 1) + \
                   convert2bin(high_volt_protection, 1) + \
                   convert2bin(high_voltage_point, 5)


    elif (command_id == 9):

        timer_number = int(request.GET.get('tn'))
        contr_obj = Controller.objects.get(id=data_id)

        timer = Timer.objects.get(controller=contr_obj,
                                  timer_number=timer_number)

        week_days = request.GET.get('wd', timer.week_days)
        timer.week_days = week_days

        if int(week_days) in [0,1,2]:
            timer_enable = 1
        else:
            timer_enable = 0

        timer.timer_enable = timer_enable

        hours = request.GET.get('h', timer.hours)
        timer.hours = hours

        m = request.GET.get('m', timer.m)
        timer.m = m

        timer.save()

        PayloadA = convert2bin(timer_enable, 1) + convert2bin(week_days, 2) + convert2bin(hours, 5)
        PayloadB = convert2bin(timer_number, 3) + convert2bin(m, 5)


    elif (command_id == 10):

        timer_number = int(request.GET.get('tn'))
        contr_obj = Controller.objects.get(id=data_id)

        timer = Timer.objects.get(controller=contr_obj,
                                  timer_number=timer_number)


        max_duration_hours = request.GET.get('mdh', timer.max_duration_hours)
        timer.max_duration_hours = max_duration_hours

        max_duration_minutes = request.GET.get('mdm', timer.max_duration_minutes)
        timer.max_duration_minutes = max_duration_minutes

        timer.save()

        PayloadA = "000" + convert2bin(max_duration_hours, 5)
        PayloadB = convert2bin(timer_number, 3) + convert2bin(max_duration_minutes, 5)

    elif (command_id == 11):
        week_days = request.GET.get('wd', controller.timer_days)
        controller.master_week_days = week_days

        hours = request.GET.get('h', controller.hours)
        controller.master_hours = hours

        m = request.GET.get('m', controller.m)
        controller.master_minutes = m

        PayloadA = convert2bin(week_days, 3) + convert2bin(hours, 5)
        PayloadB = "00" + convert2bin(m, 6)


    elif (command_id == 12):
        pass

    elif (command_id == 13):
        onoff = int(request.GET.get('onoff'))
        controller.onoff = onoff
        if onoff == 1:
            PayloadA = "00000000"
            PayloadB = "00000001"
        else:
            PayloadA = "00000000"
            PayloadB = "00000010"


    elif (command_id == 14):
        license_type = request.GET.get('lt', controller.license_type)
        controller.license_type = license_type

        select_motor = request.GET.get('sm', controller.select_motor)
        controller.select_motor = select_motor

        mmo = request.GET.get('mmo', controller.max_motor_on)
        controller.max_motor_on = mmo

        # placeholders for now
        PayloadA = "01101001"
        PayloadB = "00111001"

    elif (command_id == 101):
        license_type = request.GET.get('lt', controller.license_type)
        controller.license_type = license_type

        select_motor = request.GET.get('sm', controller.select_motor)
        controller.select_motor = select_motor

        mmo = request.GET.get('mmo', controller.max_motor_on)
        controller.max_motor_on = mmo

        # placeholders for now
        PayloadA = "01101001"
        PayloadB = "00111001"

    elif (command_id == 102):
        graphical_or_not = request.GET.get('gon', 0)
        controller.graphical_or_not = graphical_or_not
        Controller.objects.all().filter(device_id=controller.device_id)\
            .update(graphical_or_not=graphical_or_not)
        numerical_or_not = request.GET.get('non', 0)
        controller.numerical_or_not = numerical_or_not
        # placeholders for now
        PayloadA = "01101001"
        PayloadB = "00111001"

    elif (command_id == 103):
        manual_or_not = request.GET.get('mon', 0)
        controller.manual_or_not = manual_or_not
        auto_or_not = request.GET.get('aon', 0)
        controller.auto_or_not = auto_or_not

        # placeholders for now
        PayloadA = "01101001"
        PayloadB = "00111001"

    elif (command_id == 104):
        display_scroll_seconds = request.GET.get('st', controller.display_scroll_seconds)
        controller.display_scroll_seconds = display_scroll_seconds

        # placeholders for now
        PayloadA = "01101001"
        PayloadB = "00111001"

    elif (command_id == 105):
        sub_ID = request.GET.get('sub_id')
        tank = Tank.objects.get(controller=controller, sub_ID=sub_ID)
        new_name = request.GET.get('new_name')
        tank.name = new_name
        tank.save()

    elif (command_id == 106):
        PayloadA = "00000000"
        PayloadB = "00000100"
        command_byte = "00001101"

    '''elif(command_id==12):
        pass


    elif(command_id==13):
        pass'''

    data_stream = idno + command_byte + PayloadA + PayloadB
    # print data_stream
    send_string(data_stream)

    controller.save()




def send_string(controller_data_to_send):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (TCP_SERVER_IP, TCP_SERVER_PORT)
    sock.connect(server_address)

    try:
        message = 'send ' + controller_data_to_send
        sock.sendall(message)
        print message
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
    if (length - l > 0):
        for i in range(0, (length - l)):
            s = s + "0"
        return (s + a)
    else:
        return a


def convert_bin_to_char(bin_text):
    return unichr(int(bin_text, 2))


def generate_log(request):
    displayed = 0
    filename = file_locations_and_constants.LOG_FILE_LOCATION
    result = ''
    for line in reversed(open(filename).readlines()):
        result += line + '\n'
        displayed += 1
        if displayed > 1000:
            break

    return HttpResponse(result, content_type='text/plain')

