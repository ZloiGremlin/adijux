# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PageTranslation.submenu'
        db.add_column('pages_page_translation', 'submenu',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PageTranslation.submenu'
        db.delete_column('pages_page_translation', 'submenu')


    models = {
        'gallery.album': {
            'Meta': {'object_name': 'Album'},
            'gallery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pages.block': {
            'Meta': {'object_name': 'Block'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pages.blocktranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'BlockTranslation', 'db_table': "'pages_block_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['pages.Block']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'pages.menu': {
            'Meta': {'ordering': "['sort']", 'object_name': 'Menu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'menus'", 'null': 'True', 'to': "orm['pages.Page']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['pages.Menu']"}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'top'", 'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'pages.menutranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'MenuTranslation', 'db_table': "'pages_menu_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['pages.Menu']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pages.page': {
            'Meta': {'object_name': 'Page'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Album']", 'null': 'True', 'blank': 'True'}),
            'front': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'pages.pagetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PageTranslation', 'db_table': "'pages_page_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['pages.Page']"}),
            'menu': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'submenu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pages']