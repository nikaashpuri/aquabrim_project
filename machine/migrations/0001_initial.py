# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Device'
        db.create_table(u'machine_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('field_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'machine', ['Device'])


    def backwards(self, orm):
        # Deleting model 'Device'
        db.delete_table(u'machine_device')


    models = {
        u'machine.device': {
            'Meta': {'object_name': 'Device'},
            'field_1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'field_2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['machine']