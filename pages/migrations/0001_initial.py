# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PageTranslation'
        db.create_table('pages_page_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('menu', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['pages.Page'])),
        ))
        db.send_create_signal('pages', ['PageTranslation'])

        # Adding unique constraint on 'PageTranslation', fields ['language_code', 'master']
        db.create_unique('pages_page_translation', ['language_code', 'master_id'])

        # Adding model 'Page'
        db.create_table('pages_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('front', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('pages', ['Page'])

        # Adding model 'BlockTranslation'
        db.create_table('pages_block_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['pages.Block'])),
        ))
        db.send_create_signal('pages', ['BlockTranslation'])

        # Adding unique constraint on 'BlockTranslation', fields ['language_code', 'master']
        db.create_unique('pages_block_translation', ['language_code', 'master_id'])

        # Adding model 'Block'
        db.create_table('pages_block', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('pages', ['Block'])

        # Adding model 'MenuTranslation'
        db.create_table('pages_menu_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['pages.Menu'])),
        ))
        db.send_create_signal('pages', ['MenuTranslation'])

        # Adding unique constraint on 'MenuTranslation', fields ['language_code', 'master']
        db.create_unique('pages_menu_translation', ['language_code', 'master_id'])

        # Adding model 'Menu'
        db.create_table('pages_menu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('pages', ['Menu'])

        # Adding M2M table for field page on 'Menu'
        db.create_table('pages_menu_page', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('menu', models.ForeignKey(orm['pages.menu'], null=False)),
            ('page', models.ForeignKey(orm['pages.page'], null=False))
        ))
        db.create_unique('pages_menu_page', ['menu_id', 'page_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'MenuTranslation', fields ['language_code', 'master']
        db.delete_unique('pages_menu_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'BlockTranslation', fields ['language_code', 'master']
        db.delete_unique('pages_block_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'PageTranslation', fields ['language_code', 'master']
        db.delete_unique('pages_page_translation', ['language_code', 'master_id'])

        # Deleting model 'PageTranslation'
        db.delete_table('pages_page_translation')

        # Deleting model 'Page'
        db.delete_table('pages_page')

        # Deleting model 'BlockTranslation'
        db.delete_table('pages_block_translation')

        # Deleting model 'Block'
        db.delete_table('pages_block')

        # Deleting model 'MenuTranslation'
        db.delete_table('pages_menu_translation')

        # Deleting model 'Menu'
        db.delete_table('pages_menu')

        # Removing M2M table for field page on 'Menu'
        db.delete_table('pages_menu_page')


    models = {
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
            'Meta': {'object_name': 'Menu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'menus'", 'symmetrical': 'False', 'to': "orm['pages.Page']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pages.menutranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'MenuTranslation', 'db_table': "'pages_menu_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['pages.Menu']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pages.page': {
            'Meta': {'ordering': "['sort']", 'object_name': 'Page'},
            'front': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
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
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pages']