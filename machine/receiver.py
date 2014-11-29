__author__ = 'shubham_dokania'


def ConvertAndSave(Controller, s = '000000000000000000000000000000111111111111110101'):
    array = []
    for i in range(0, 6):
        array.append(s[(i*8):((i+1)*8)])

    idno = int(str(int(array[0], 2))+str(int(array[1], 2))+str(int(array[2], 2)))
    print idno
    obj = Controller.objects.get(device_id=idno)
    command = int(array[3], 2)

    PA = array[4]
    PB = array[5]

    if command==1:
        #------------------------for Payload A---------------------------#
        '''consedering that the sub-ID is a number decoded in 6-bit binary'''
        sub_id = int(PA[0:6], 2)
        overflow_stat = PA[6]
        flow_stat = PA[7]
        #------------------------for Payload B----------------------------#
        water_level = int(PB[1:8], 2)

        obj.sub_ID = str(sub_id)
        obj.overflow_status = overflow_stat
        obj.flow_status = flow_stat
        obj.water_level = water_level

    elif(command==2):
        #---------------------for Payload A and B-------------------------#
        print "For Future use!!!"

    elif(command==3):
        #------------------------for Payload A---------------------------#
        sub_id = int(PA[0:6], 2)
        AF = PA[6]
        AL = PA[7]

        #------------------------for Payload B---------------------------#
        M = PB[0]
        F = PB[1]
        E = PB[2]
        Ns = int(PB[3:8], 2)

        obj.low_level_alarm = AL
        obj.full_level_alarm = AF
        obj.sub_ID = sub_id
        obj.motor_trigger = M
        obj.flow_protection = F
        obj.enable_disable = E
        obj.no_signal_duration = Ns


    elif(command==4):
        #------------------------for Payload A---------------------------#
        #NOTHING TO DO HERE!!!
        #------------------------for Payload B---------------------------#
        Mode = int(PB[6:8], 2)
        Tr = int(PB[0], 2)
        D = int(PB[1:5], 2)
        T = int(PB[5], 2)

        obj.mode_selection = Mode
        obj.trial_enabled = Tr
        obj.timer_based = T
        obj.trial_period = D

    elif(command==5):
        #------------------------for Payload A---------------------------#
        Tx = int(PA[0:2], 2)
        W = int(PA[2:4], 2)
        O = int(PA[4:8], 2)
        #------------------------for Payload B---------------------------#
        L = int(PB[0:8], 2)

        obj.Tx_type = Tx
        obj.water_level_type = W
        obj.offset_level_reset = O
        obj.water_level = L

    elif(command==6):
        #------------------------for Payload A---------------------------#
        Rd = int(PA[0:3], 2)
        Tg = int(PA[4:8], 2)
        #------------------------for Payload B---------------------------#
        Td = int(PB[0:4], 2)
        N = int(PB[4:6], 2)
        M_operating = int(PB[6:8], 2)

        obj.restart_delay = Rd
        obj.trial_gap = Tg
        obj.trial_duration = Td
        obj.trials = N
        obj.operating_mn = M_operating


    elif(command==7):
        #------------------------for Payload A---------------------------#
        Sd = int(PA[3:7], 2)
        En = int(PA[7], 2)
        #------------------------for Payload B---------------------------#
        To = int(PB[0:8], 2)

        obj.initial_start_delay = Sd
        obj.timeout_protection = En
        obj.timeout_duration = To

    elif(command==8):
        #------------------------for Payload A---------------------------#
        En = int(PA[0], 2)
        Ov = int(PA[1:5], 2)
        LE = int(PA[5], 2)
        Lv = int(str(PA[6:8])+str(PB[0:2]))
        Lv = int(Lv, 2)
        #------------------------for Payload B---------------------------#
        HE = int(PB[2], 2)
        Hv = int(PB[3:8], 2)

        obj.voltage_enable = En
        obj.high_voltage_point = Hv
        obj.low_voltage_point = Lv
        obj.offset_voltage = Ov
        obj.low_volt_protection = LE
        obj.high_volt_protection = HE

    elif(command==9):
        #------------------------for Payload A---------------------------#
        Dy = int(PA[0:3], 2)
        H = int(PA[3:8], 2)
        #------------------------for Payload B---------------------------#
        En = int(PB[0], 2)
        Tn = int(PB[1:4], 2)
        M = int(PB[4:8], 2)

        obj.week_days = Dy
        obj.timer_enable = En
        obj.hours = H
        obj.timer_number = Tn
        '''LOOK AT THIS ISSUE'''
        #NO IDEA WHAT THIS "M" IS DOING HERE!!!! LOOK AT THIS!!!!

    elif(command==10):
        #------------------------for Payload A---------------------------#
        Dy = int(PA[0:3], 2)
        H = int(PA[3:8], 2)
        #------------------------for Payload B---------------------------#
        M = int(PB[2:8], 2)

        obj.week_days = Dy
        obj.hours = H
        #AGAIN THIS "M" COMES UP!!!

    elif(command==11):
        #------------------------for Payload A---------------------------#
        NS = int(PA[7], 2)
        #------------------------for Payload B---------------------------#
        NT = int(PB[0], 2)
        Mn = int(PB[1], 2)
        MO = int(PB[2], 2)
        FE = int(PB[3], 2)
        TO = int(PB[4], 2)
        VH = int(PB[5], 2)
        VL = int(PB[6], 2)
        Tx = int(PB[7], 2)

        obj.Tx_alarm = Tx
        obj.high_voltage_alarm = VH
        obj.low_voltage_alarm = VL
        obj.timeout_alarm = TO
        obj.flow_error_alarm = FE
        obj.motor_on_alarm = MO
        obj.manual_motor_on_alarm = Mn
        obj.no_signal_alarm_top = NT
        obj.no_signal_alarm_sump = NS

    elif(command==12):
        print "Accept another Tx Data!!"

    else:
        print "SOMETHING SEEMS TO BE WRONG HERE!!!!! GO AWAY!!!!"

    obj.save()

