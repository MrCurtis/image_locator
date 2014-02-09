# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'selectedImage'
        db.create_table(u'image_locator_app_selectedimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('lattitude', self.gf('django.db.models.fields.FloatField')()),
            ('longtitude', self.gf('django.db.models.fields.FloatField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'image_locator_app', ['selectedImage'])


    def backwards(self, orm):
        # Deleting model 'selectedImage'
        db.delete_table(u'image_locator_app_selectedimage')


    models = {
        u'image_locator_app.selectedimage': {
            'Meta': {'object_name': 'selectedImage'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'lattitude': ('django.db.models.fields.FloatField', [], {}),
            'longtitude': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['image_locator_app']