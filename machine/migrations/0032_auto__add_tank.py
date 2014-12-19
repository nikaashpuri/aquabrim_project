# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tank'
        db.create_table(u'machine_tank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('controller', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['machine.Controller'])),
            ('signal_status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('overflow_status', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('sub_ID', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('motor_trigger', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('low_level_alarm', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('full_level_alarm', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('overflow_alarm', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('water_level', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('offset_level_reset', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('water_level_type', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('full_water_level', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('low_water_level', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('display', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('machine', ['Tank'])


    def backwards(self, orm):
        # Deleting model 'Tank'
        db.delete_table(u'machine_tank')


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
        'machine.command': {
            'Meta': {'object_name': 'Command'},
            'electronic_format': ('django.db.models.fields.TextField', [], {}),
            'enabled': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'machine.controller': {
            'Meta': {'object_name': 'Controller'},
            'Tx_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'Tx_type': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'auto_or_not': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'comm_error_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'current': ('django.db.models.fields.FloatField', [], {}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'display': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'display_scroll_seconds': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'enable_disable': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'flow_error_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'flow_protection': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'flow_status': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'full_level_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'full_water_level': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'graphical_or_not': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'high_volt_protection': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'high_voltage_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'high_voltage_point': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'hold': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'hours': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_start_delay': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {}),
            'license_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'line_water_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'low_level_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'low_volt_protection': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'low_voltage_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'low_voltage_point': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'low_water_level': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'machine_status': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'manual_motor_on_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'manual_or_not': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'master_hours': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'master_minutes': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'master_week_days': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'max_duration_hours': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'max_duration_minutes': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'max_motor_on': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mode_selection': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'motor_on_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'motor_status': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'motor_trigger': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'no_signal_alarm_sump': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'no_signal_alarm_top': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'no_signal_duration': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'numerical_or_not': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'offset_level_reset': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'offset_voltage': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'onStatus': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'onoff': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'operating_mn': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'overflow_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'overflow_status': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'power_factor': ('django.db.models.fields.FloatField', [], {}),
            'reset_interval': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'restart_delay': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'select_motor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'signal_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sub_ID': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'timeout_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timeout_duration': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timeout_interval': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timeout_protection': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timeout_status': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'timer_based': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timer_days': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'timer_enable': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timer_number': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'trial_duration': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'trial_enabled': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'trial_gap': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'trial_period': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'trials': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'voltage': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'voltage_enable': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'voltage_status': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'voltage_y': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'voltage_z': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'water_level': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'water_level_type': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'week_days': ('django.db.models.fields.IntegerField', [], {'max_length': '100'})
        },
        'machine.tank': {
            'Meta': {'object_name': 'Tank'},
            'controller': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machine.Controller']"}),
            'display': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'full_level_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'full_water_level': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {}),
            'low_level_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'low_water_level': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'motor_trigger': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'offset_level_reset': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'overflow_alarm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'overflow_status': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'signal_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sub_ID': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'water_level': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'water_level_type': ('django.db.models.fields.IntegerField', [], {'max_length': '100'})
        },
        'machine.timer': {
            'Meta': {'object_name': 'Timer'},
            'controller': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machine.Controller']"}),
            'hours': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'max_duration_hours': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'max_duration_minutes': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timer_enable': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timer_number': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'week_days': ('django.db.models.fields.IntegerField', [], {'max_length': '100'})
        },
        'machine.transmitter': {
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