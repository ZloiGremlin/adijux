# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RoomBooking.place'
        db.add_column('room_roombooking', 'place',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RoomBooking.place'
        db.delete_column('room_roombooking', 'place')


    models = {
        'room.room': {
            'Meta': {'object_name': 'Room'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'room.roombooking': {
            'Meta': {'object_name': 'RoomBooking'},
            'bed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cart': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'people': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'qty': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'booking'", 'to': "orm['room.Room']"}),
            'window': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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