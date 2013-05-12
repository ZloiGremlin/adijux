# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RoomDates'
        db.create_table('room_roomdates', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dates', to=orm['room.Room'])),
            ('date_from', self.gf('django.db.models.fields.DateField')()),
            ('date_to', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('room', ['RoomDates'])


    def backwards(self, orm):
        # Deleting model 'RoomDates'
        db.delete_table('room_roomdates')


    models = {
        'room.room': {
            'Meta': {'object_name': 'Room'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'room.roomdates': {
            'Meta': {'object_name': 'RoomDates'},
            'date_from': ('django.db.models.fields.DateField', [], {}),
            'date_to': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dates'", 'to': "orm['room.Room']"})
        },
        'room.roomimages': {
            'Meta': {'object_name': 'RoomImages'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['room.Room']"})
        },
        'room.roomtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'RoomTranslation', 'db_table': "'room_room_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['room.Room']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['room']