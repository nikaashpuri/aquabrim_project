# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Controller.onoff'
        db.add_column(u'machine_controller', 'onoff',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=5),
                      keep_default=False)

        # Adding field 'Controller.hold'
        db.add_column(u'machine_controller', 'hold',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=5),
                      keep_default=False)

        # Adding field 'Controller.voltage_status'
        db.add_column(u'machine_controller', 'voltage_status',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=5),
                      keep_default=False)

        # Adding field 'Controller.timeout_status'
        db.add_column(u'machine_controller', 'timeout_status',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=5),
                      keep_default=False)


        # Changing field 'Controller.motor_status'
        db.alter_column(u'machine_controller', 'motor_status', self.gf('django.db.models.fields.IntegerField')(max_length=10))

        # Changing field 'Controller.machine_status'
        db.alter_column(u'machine_controller', 'machine_status', self.gf('django.db.models.fields.IntegerField')(max_length=100))

        # Changing field 'Controller.voltage'
        db.alter_column(u'machine_controller', 'voltage', self.gf('django.db.models.fields.IntegerField')(max_length=10))

        # Changing field 'Controller.timeout_interval'
        db.alter_column(u'machine_controller', 'timeout_interval', self.gf('django.db.models.fields.IntegerField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'Controller.onoff'
        db.delete_column(u'machine_controller', 'onoff')

        # Deleting field 'Controller.hold'
        db.delete_column(u'machine_controller', 'hold')

        # Deleting field 'Controller.voltage_status'
        db.delete_column(u'machine_controller', 'voltage_status')

        # Deleting field 'Controller.timeout_status'
        db.delete_column(u'machine_controller', 'timeout_status')


        # Changing field 'Controller.motor_status'
        db.alter_column(u'machine_controller', 'motor_status', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Controller.machine_status'
        db.alter_column(u'machine_controller', 'machine_status', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Controller.voltage'
        db.alter_column(u'machine_controller', 'voltage', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Controller.timeout_interval'
        db.alter_column(u'machine_controller', 'timeout_interval', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'device_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'hold': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'machine_status': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'motor_status': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'onoff': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'signal_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'timeout_interval': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'timeout_status': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'voltage': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'voltage_status': ('django.db.models.fields.IntegerField', [], {'max_length': '5'})
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