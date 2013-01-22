# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RoomTranslation'
        db.create_table('room_room_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['room.Room'])),
        ))
        db.send_create_signal('room', ['RoomTranslation'])

        # Adding unique constraint on 'RoomTranslation', fields ['language_code', 'master']
        db.create_unique('room_room_translation', ['language_code', 'master_id'])

        # Adding model 'Room'
        db.create_table('room_room', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('room', ['Room'])

        # Adding model 'RoomImages'
        db.create_table('room_roomimages', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['room.Room'])),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal('room', ['RoomImages'])


    def backwards(self, orm):
        # Removing unique constraint on 'RoomTranslation', fields ['language_code', 'master']
        db.delete_unique('room_room_translation', ['language_code', 'master_id'])

        # Deleting model 'RoomTranslation'
        db.delete_table('room_room_translation')

        # Deleting model 'Room'
        db.delete_table('room_room')

        # Deleting model 'RoomImages'
        db.delete_table('room_roomimages')


    models = {
        'room.room': {
            'Meta': {'object_name': 'Room'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'room.roomimages': {
            'Meta': {'object_name': 'RoomImages'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['room.Room']"})
        },
        'room.roomtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'RoomTranslation', 'db_table': "'room_room_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['room.Room']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['room']