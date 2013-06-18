# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table('gallery_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('gallery', ['Album'])

        # Adding field 'ImageElement.album'
        db.add_column('gallery_imageelement', 'album',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['gallery.Album']),
                      keep_default=False)


        # Changing field 'ImageElement.image'
        db.alter_column('gallery_imageelement', 'image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100))

    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table('gallery_album')

        # Deleting field 'ImageElement.album'
        db.delete_column('gallery_imageelement', 'album_id')


        # Changing field 'ImageElement.image'
        db.alter_column('gallery_imageelement', 'image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

    models = {
        'gallery.album': {
            'Meta': {'object_name': 'Album'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'gallery.imageelement': {
            'Meta': {'object_name': 'ImageElement'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['gallery.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'})
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