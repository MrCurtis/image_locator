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
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('altitude', self.gf('django.db.models.fields.FloatField')()),
            ('heading', self.gf('django.db.models.fields.FloatField')()),
            ('tilt', self.gf('django.db.models.fields.FloatField')()),
            ('roll', self.gf('django.db.models.fields.FloatField')()),
            ('water', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sanitation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('food', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('shelter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('medicine', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('protection', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('obstruction', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'image_locator_app', ['DroneImage'])


    def backwards(self, orm):
        # Deleting model 'DroneImage'
        db.delete_table(u'image_locator_app_droneimage')


    models = {
        u'image_locator_app.droneimage': {
            'Meta': {'object_name': 'DroneImage'},
            'altitude': ('django.db.models.fields.FloatField', [], {}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'food': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'heading': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'medicine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'obstruction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'protection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'roll': ('django.db.models.fields.FloatField', [], {}),
            'sanitation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shelter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tilt': ('django.db.models.fields.FloatField', [], {}),
            'water': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['image_locator_app']