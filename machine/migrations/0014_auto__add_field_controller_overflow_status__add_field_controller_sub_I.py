# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Controller.overflow_status'
        db.add_column(u'machine_controller', 'overflow_status',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.sub_ID'
        db.add_column(u'machine_controller', 'sub_ID',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.flow_status'
        db.add_column(u'machine_controller', 'flow_status',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.enable_disable'
        db.add_column(u'machine_controller', 'enable_disable',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.flow_protection'
        db.add_column(u'machine_controller', 'flow_protection',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.motor_trigger'
        db.add_column(u'machine_controller', 'motor_trigger',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.low_level_alarm'
        db.add_column(u'machine_controller', 'low_level_alarm',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.full_level_alarm'
        db.add_column(u'machine_controller', 'full_level_alarm',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.overflow_alarm'
        db.add_column(u'machine_controller', 'overflow_alarm',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.no_signal_duration'
        db.add_column(u'machine_controller', 'no_signal_duration',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.mode_selection'
        db.add_column(u'machine_controller', 'mode_selection',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.Tx_type'
        db.add_column(u'machine_controller', 'Tx_type',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.water_level'
        db.add_column(u'machine_controller', 'water_level',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.offset_level_reset'
        db.add_column(u'machine_controller', 'offset_level_reset',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.water_level_type'
        db.add_column(u'machine_controller', 'water_level_type',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.operating_mn'
        db.add_column(u'machine_controller', 'operating_mn',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.trials'
        db.add_column(u'machine_controller', 'trials',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.trial_duration'
        db.add_column(u'machine_controller', 'trial_duration',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.trial_gap'
        db.add_column(u'machine_controller', 'trial_gap',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.restart_delay'
        db.add_column(u'machine_controller', 'restart_delay',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.timeout_duration'
        db.add_column(u'machine_controller', 'timeout_duration',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.timeout_protection'
        db.add_column(u'machine_controller', 'timeout_protection',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.initial_start_delay'
        db.add_column(u'machine_controller', 'initial_start_delay',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.high_voltage_point'
        db.add_column(u'machine_controller', 'high_voltage_point',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.low_voltage_point'
        db.add_column(u'machine_controller', 'low_voltage_point',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.offset_voltage'
        db.add_column(u'machine_controller', 'offset_voltage',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.high_volt_protection'
        db.add_column(u'machine_controller', 'high_volt_protection',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.low_volt_protection'
        db.add_column(u'machine_controller', 'low_volt_protection',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.timer_enable'
        db.add_column(u'machine_controller', 'timer_enable',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.week_days'
        db.add_column(u'machine_controller', 'week_days',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.timer_number'
        db.add_column(u'machine_controller', 'timer_number',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.hours'
        db.add_column(u'machine_controller', 'hours',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.Tx_alarm'
        db.add_column(u'machine_controller', 'Tx_alarm',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.low_voltage_alarm'
        db.add_column(u'machine_controller', 'low_voltage_alarm',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.high_voltage_alarm'
        db.add_column(u'machine_controller', 'high_voltage_alarm',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.timeout_alarm'
        db.add_column(u'machine_controller', 'timeout_alarm',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.flow_error_alarm'
        db.add_column(u'machine_controller', 'flow_error_alarm',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.motor_on_alarm'
        db.add_column(u'machine_controller', 'motor_on_alarm',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.manual_motor_on_alarm'
        db.add_column(u'machine_controller', 'manual_motor_on_alarm',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.no_signal_alarm_tomp'
        db.add_column(u'machine_controller', 'no_signal_alarm_tomp',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'Controller.no_signal_alarm_sump'
        db.add_column(u'machine_controller', 'no_signal_alarm_sump',
                      self.gf('django.db.models.fields.IntegerField')(default=2, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Controller.overflow_status'
        db.delete_column(u'machine_controller', 'overflow_status')

        # Deleting field 'Controller.sub_ID'
        db.delete_column(u'machine_controller', 'sub_ID')

        # Deleting field 'Controller.flow_status'
        db.delete_column(u'machine_controller', 'flow_status')

        # Deleting field 'Controller.enable_disable'
        db.delete_column(u'machine_controller', 'enable_disable')

        # Deleting field 'Controller.flow_protection'
        db.delete_column(u'machine_controller', 'flow_protection')

        # Deleting field 'Controller.motor_trigger'
        db.delete_column(u'machine_controller', 'motor_trigger')

        # Deleting field 'Controller.low_level_alarm'
        db.delete_column(u'machine_controller', 'low_level_alarm')

        # Deleting field 'Controller.full_level_alarm'
        db.delete_column(u'machine_controller', 'full_level_alarm')

        # Deleting field 'Controller.overflow_alarm'
        db.delete_column(u'machine_controller', 'overflow_alarm')

        # Deleting field 'Controller.no_signal_duration'
        db.delete_column(u'machine_controller', 'no_signal_duration')

        # Deleting field 'Controller.mode_selection'
        db.delete_column(u'machine_controller', 'mode_selection')

        # Deleting field 'Controller.Tx_type'
        db.delete_column(u'machine_controller', 'Tx_type')

        # Deleting field 'Controller.water_level'
        db.delete_column(u'machine_controller', 'water_level')

        # Deleting field 'Controller.offset_level_reset'
        db.delete_column(u'machine_controller', 'offset_level_reset')

        # Deleting field 'Controller.water_level_type'
        db.delete_column(u'machine_controller', 'water_level_type')

        # Deleting field 'Controller.operating_mn'
        db.delete_column(u'machine_controller', 'operating_mn')

        # Deleting field 'Controller.trials'
        db.delete_column(u'machine_controller', 'trials')

        # Deleting field 'Controller.trial_duration'
        db.delete_column(u'machine_controller', 'trial_duration')

        # Deleting field 'Controller.trial_gap'
        db.delete_column(u'machine_controller', 'trial_gap')

        # Deleting field 'Controller.restart_delay'
        db.delete_column(u'machine_controller', 'restart_delay')

        # Deleting field 'Controller.timeout_duration'
        db.delete_column(u'machine_controller', 'timeout_duration')

        # Deleting field 'Controller.timeout_protection'
        db.delete_column(u'machine_controller', 'timeout_protection')

        # Deleting field 'Controller.initial_start_delay'
        db.delete_column(u'machine_controller', 'initial_start_delay')

        # Deleting field 'Controller.high_voltage_point'
        db.delete_column(u'machine_controller', 'high_voltage_point')

        # Deleting field 'Controller.low_voltage_point'
        db.delete_column(u'machine_controller', 'low_voltage_point')

        # Deleting field 'Controller.offset_voltage'
        db.delete_column(u'machine_controller', 'offset_voltage')

        # Deleting field 'Controller.high_volt_protection'
        db.delete_column(u'machine_controller', 'high_volt_protection')

        # Deleting field 'Controller.low_volt_protection'
        db.delete_column(u'machine_controller', 'low_volt_protection')

        # Deleting field 'Controller.timer_enable'
        db.delete_column(u'machine_controller', 'timer_enable')

        # Deleting field 'Controller.week_days'
        db.delete_column(u'machine_controller', 'week_days')

        # Deleting field 'Controller.timer_number'
        db.delete_column(u'machine_controller', 'timer_number')

        # Deleting field 'Controller.hours'
        db.delete_column(u'machine_controller', 'hours')

        # Deleting field 'Controller.Tx_alarm'
        db.delete_column(u'machine_controller', 'Tx_alarm')

        # Deleting field 'Controller.low_voltage_alarm'
        db.delete_column(u'machine_controller', 'low_voltage_alarm')

        # Deleting field 'Controller.high_voltage_alarm'
        db.delete_column(u'machine_controller', 'high_voltage_alarm')

        # Deleting field 'Controller.timeout_alarm'
        db.delete_column(u'machine_controller', 'timeout_alarm')

        # Deleting field 'Controller.flow_error_alarm'
        db.delete_column(u'machine_controller', 'flow_error_alarm')

        # Deleting field 'Controller.motor_on_alarm'
        db.delete_column(u'machine_controller', 'motor_on_alarm')

        # Deleting field 'Controller.manual_motor_on_alarm'
        db.delete_column(u'machine_controller', 'manual_motor_on_alarm')

        # Deleting field 'Controller.no_signal_alarm_tomp'
        db.delete_column(u'machine_controller', 'no_signal_alarm_tomp')

        # Deleting field 'Controller.no_signal_alarm_sump'
        db.delete_column(u'machine_controller', 'no_signal_alarm_sump')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'machine.command': {
            'Meta': {'object_name': 'Command'},
            'electronic_format': ('django.db.models.fields.TextField', [], {}),
            'enabled': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'machine.controller': {
            'Meta': {'object_name': 'Controller'},
            'Tx_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'Tx_type': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'device_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'enable_disable': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'flow_error_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'flow_protection': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'flow_status': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'full_level_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'high_volt_protection': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'high_voltage_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'high_voltage_point': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'hold': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'hours': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_start_delay': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'low_level_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'low_volt_protection': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'low_voltage_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'low_voltage_point': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'machine_status': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'manual_motor_on_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'mode_selection': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'motor_on_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'motor_status': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'motor_trigger': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'no_signal_alarm_sump': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'no_signal_alarm_tomp': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'no_signal_duration': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'offset_level_reset': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'offset_voltage': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'onStatus': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'onoff': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'operating_mn': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'overflow_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'overflow_status': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'restart_delay': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'signal_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sub_ID': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'timeout_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timeout_duration': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timeout_interval': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timeout_protection': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timeout_status': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'timer_enable': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timer_number': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'trial_duration': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'trial_gap': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'trials': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'voltage': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'voltage_status': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'water_level': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'water_level_type': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'week_days': ('django.db.models.fields.IntegerField', [], {'max_length': '100'})
        },
        u'machine.transmitter': {
            'Meta': {'object_name': 'Transmitter'},
            'device_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'flow_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'sub_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tank_25_full': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tank_50_full': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tank_75_full': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['machine']