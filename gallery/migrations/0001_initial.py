# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageElementTranslation'
        db.create_table('gallery_imageelement_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['gallery.ImageElement'])),
        ))
        db.send_create_signal('gallery', ['ImageElementTranslation'])

        # Adding unique constraint on 'ImageElementTranslation', fields ['language_code', 'master']
        db.create_unique('gallery_imageelement_translation', ['language_code', 'master_id'])

        # Adding model 'ImageElement'
        db.create_table('gallery_imageelement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('gallery', ['ImageElement'])


    def backwards(self, orm):
        # Removing unique constraint on 'ImageElementTranslation', fields ['language_code', 'master']
        db.delete_unique('gallery_imageelement_translation', ['language_code', 'master_id'])

        # Deleting model 'ImageElementTranslation'
        db.delete_table('gallery_imageelement_translation')

        # Deleting model 'ImageElement'
        db.delete_table('gallery_imageelement')


    models = {
        'gallery.imageelement': {
            'Meta': {'object_name': 'ImageElement'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'gallery.imageelementtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ImageElementTranslation', 'db_table': "'gallery_imageelement_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['gallery.ImageElement']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['gallery']