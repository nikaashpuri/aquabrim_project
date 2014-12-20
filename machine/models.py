from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
# Create your models here.


class Transmitter(models.Model):
    user = models.ForeignKey(User)
    device_id = models.CharField(max_length = 100, unique=True)
    sub_id = models.CharField(max_length = 100)
    tank_75_full = models.CharField(max_length = 10)
    tank_50_full = models.CharField(max_length = 10)
    tank_25_full = models.CharField(max_length = 10)
    flow_status = models.CharField(max_length = 10)
    timestamp = models.DateTimeField()
    ip_address = models.CharField(max_length = 200, null=True)

    class Meta:
        app_label = 'machine'


class Controller(models.Model):
    user = models.ForeignKey(User)
    device_id = models.CharField(max_length = 100)
    timestamp = models.DateTimeField()
    motor_status = models.IntegerField(max_length = 10)

    signal_status = models.CharField(max_length = 10)
    voltage = models.IntegerField(max_length = 10)
    name = models.CharField(max_length = 100)
    timeout_interval = models.IntegerField(max_length = 100)

    machine_status = models.IntegerField(max_length = 100)
    onoff = models.IntegerField(max_length=5)
    hold = models.IntegerField(max_length=5)

    voltage_status = models.IntegerField(max_length=5)
    timeout_status = models.IntegerField(max_length=5)
    onStatus = models.CharField(max_length=10)

    #newly added!!!

    flow_status = models.IntegerField(max_length=100)
    enable_disable = models.IntegerField(max_length=100)
    flow_protection = models.IntegerField(max_length=100)

    motor_trigger = models.IntegerField(max_length=100)
    low_level_alarm = models.IntegerField(max_length=100)
    full_level_alarm = models.IntegerField(max_length=100)
    overflow_alarm = models.IntegerField(max_length=100)

    no_signal_duration = models.IntegerField(max_length=100)
    mode_selection = models.IntegerField(max_length=100)
    Tx_type = models.IntegerField(max_length=100)

    operating_mn = models.IntegerField(max_length=100)
    trials = models.IntegerField(max_length=100)
    trial_duration = models.IntegerField(max_length=100)

    trial_gap = models.IntegerField(max_length=100)
    restart_delay = models.IntegerField(max_length=100)
    timeout_duration = models.IntegerField(max_length=100)
    timeout_protection = models.IntegerField(max_length=100)

    voltage_enable = models.IntegerField(max_length=100)
    initial_start_delay = models.IntegerField(max_length=100)
    high_voltage_point = models.IntegerField(max_length=100)
    low_voltage_point = models.IntegerField(max_length=100)

    offset_voltage = models.IntegerField(max_length=100)
    high_volt_protection = models.IntegerField(max_length=100)
    low_volt_protection = models.IntegerField(max_length=100)
    timer_enable = models.IntegerField(max_length=100)

    week_days = models.IntegerField(max_length=100)
    timer_number = models.IntegerField(max_length=100)
    hours = models.IntegerField(max_length=100)
    Tx_alarm = models.IntegerField(max_length=100)

    low_voltage_alarm = models.IntegerField(max_length=100)
    high_voltage_alarm = models.IntegerField(max_length=100)

    timeout_alarm = models.IntegerField(max_length=100)
    flow_error_alarm = models.IntegerField(max_length=100)

    motor_on_alarm = models.IntegerField(max_length=100)
    manual_motor_on_alarm = models.IntegerField(max_length=100)

    no_signal_alarm_top = models.IntegerField(max_length=100)
    no_signal_alarm_sump = models.IntegerField(max_length=100)

    trial_enabled = models.IntegerField(max_length=100)
    timer_based = models.IntegerField(max_length=100)
    trial_period = models.IntegerField(max_length=100)
    m = models.IntegerField(max_length=100)

    # some more added for demo purpose
    license_type = models.CharField(max_length=100)
    select_motor = models.CharField(max_length=100)
    max_motor_on = models.CharField(max_length=100)


    comm_error_alarm = models.IntegerField(max_length=10)
    line_water_alarm = models.IntegerField(max_length=10)

    max_duration_hours = models.IntegerField(max_length=100)
    max_duration_minutes = models.IntegerField(max_length=100)

    graphical_or_not = models.IntegerField(max_length=100)
    numerical_or_not = models.IntegerField(max_length=100)
    manual_or_not = models.IntegerField(max_length=100)
    auto_or_not = models.IntegerField(max_length=100)
    display_scroll_seconds = models.IntegerField(max_length=100)

    timer_days = models.CharField(max_length=100)

    master_week_days = models.IntegerField(max_length=100)
    master_hours = models.IntegerField(max_length=100)
    master_minutes = models.IntegerField(max_length=100)

    reset_interval = models.IntegerField(max_length=100)

    voltage_y = models.IntegerField(max_length=100)
    voltage_z = models.IntegerField(max_length=100)
    power_factor = models.FloatField()
    current = models.FloatField()

    last_update = models.DateTimeField()

    # added for command id 4
    com_pass = models.CharField(max_length=100)
    com_m = models.IntegerField(max_length=100)
    com_t = models.IntegerField(max_length=100)
    com_tr = models.IntegerField(max_length=100)
    com_d = models.IntegerField(max_length=100)
    com_last_access_auth_or_not = models.IntegerField(max_length=100)

    def __unicode__(self):
        return self.device_id

    class Meta:
        app_label = 'machine'

class Command(models.Model):
    name = models.CharField(max_length = 100)
    electronic_format = models.TextField()
    enabled = models.CharField(max_length = 10)

    class Meta:
        app_label = 'machine'


class Timer(models.Model):
    controller = models.ForeignKey(Controller)
    week_days = models.IntegerField(max_length=100)
    timer_enable = models.IntegerField(max_length=100)
    timer_number = models.IntegerField(max_length=100)
    hours = models.IntegerField(max_length=100)
    m = models.IntegerField(max_length=100)
    max_duration_hours = models.IntegerField(max_length=100)
    max_duration_minutes = models.IntegerField(max_length=100)

    class Meta:
        app_label = 'machine'


class Tank(models.Model):
    controller = models.ForeignKey(Controller)
    name = models.CharField(max_length=100)

    #newly added!!!
    sub_ID = models.CharField(max_length=100)

    motor_trigger = models.IntegerField(max_length=100)


    low_level_alarm = models.IntegerField(max_length=100)
    full_level_alarm = models.IntegerField(max_length=100)
    overflow_alarm = models.IntegerField(max_length=100)
    current_overflow_status = models.IntegerField(max_length=100)
    no_signal_alarm = models.IntegerField(max_length=100)

    water_level = models.IntegerField(max_length=100)
    offset_level_reset = models.IntegerField(max_length=100)
    water_level_type = models.IntegerField(max_length=100)


    full_water_level = models.IntegerField(max_length=100)
    low_water_level = models.IntegerField(max_length=100)
    display = models.IntegerField(max_length=10)


    last_update = models.DateTimeField()



    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'machine'