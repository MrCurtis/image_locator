# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DroneImage'
        db.create_table(u'image_locator_app_droneimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('lattitude', self.gf('django.db.models.fields.FloatField')()),
            ('longtitude', self.gf('django.db.models.fields.FloatField')()),
            ('altitude', self.gf('django.db.models.fields.FloatField')()),
            ('heading', self.gf('django.db.models.fields.FloatField')()),
            ('tilt', self.gf('django.db.models.fields.FloatField')()),
            ('roll', self.gf('django.db.models.fields.FloatField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('interest_type', self.gf('django.db.models.fields.TextField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'image_locator_app', ['DroneImage'])


    def backwards(self, orm):
        # Deleting model 'DroneImage'
        db.delete_table(u'image_locator_app_droneimage')


    models = {
        u'image_locator_app.droneimage': {
            'Meta': {'object_name': 'DroneImage'},
            'altitude': ('django.db.models.fields.FloatField', [], {}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'heading': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'interest_type': ('django.db.models.fields.TextField', [], {}),
            'lattitude': ('django.db.models.fields.FloatField', [], {}),
            'longtitude': ('django.db.models.fields.FloatField', [], {}),
            'roll': ('django.db.models.fields.FloatField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'tilt': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['image_locator_app']