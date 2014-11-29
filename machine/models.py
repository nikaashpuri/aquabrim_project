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


class Controller(models.Model):
    user = models.ForeignKey(User)
    device_id = models.CharField(max_length = 100, unique=True)
    timestamp = models.DateTimeField()
    motor_status = models.IntegerField(max_length = 10)
    signal_status = models.CharField(max_length = 10)
    voltage = models.IntegerField(max_length = 10)
    name = models.CharField(max_length = 100)
    timeout_interval = models.IntegerField(max_length = 100)
    ip_address = models.CharField(max_length = 200, null=True)
    machine_status = models.IntegerField(max_length = 100)
    onoff = models.IntegerField(max_length=5)
    hold = models.IntegerField(max_length=5)
    voltage_status = models.IntegerField(max_length=5)
    timeout_status = models.IntegerField(max_length=5)
    onStatus = models.CharField(max_length=10)
    #newly added!!!
    overflow_status = models.IntegerField(max_length=100)
    sub_ID = models.CharField(max_length=100)
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
    water_level = models.IntegerField(max_length=100)
    offset_level_reset = models.IntegerField(max_length=100)
    water_level_type = models.IntegerField(max_length=100)
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
    



class Command(models.Model):
    name = models.CharField(max_length = 100)
    electronic_format = models.TextField()
    enabled = models.CharField(max_length = 10)

