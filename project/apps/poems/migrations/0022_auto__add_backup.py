# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Backup'
        db.create_table(u'poems_backup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('poet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poems.Poet'])),
            ('zip_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('backup_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'poems', ['Backup'])


    def backwards(self, orm):
        # Deleting model 'Backup'
        db.delete_table(u'poems_backup')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'poems.backup': {
            'Meta': {'object_name': 'Backup'},
            'backup_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poems.Poet']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'zip_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'poems.collection': {
            'Meta': {'object_name': 'Collection'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poems.Poet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '800', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'poems.fantastic': {
            'Meta': {'object_name': 'Fantastic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marked_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'on': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'poem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poems.Poem']"}),
            'reader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poems.Poet']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'poems.poem': {
            'Meta': {'ordering': "('-started_at',)", 'object_name': 'Poem'},
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'approximate_publication_date': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'audio_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poems.Poet']"}),
            'body': ('django.db.models.fields.TextField', [], {'default': "'Body'", 'null': 'True', 'blank': 'True'}),
            'display_type': ('django.db.models.fields.CharField', [], {'default': "'poetry'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'longest_line': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'public_domain': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'show_draft_revisions': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_published_revisions': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '800', 'blank': 'True'}),
            'sort_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'source_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'default': "'Title'", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'written_on': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)', 'null': 'True', 'blank': 'True'})
        },
        u'poems.poemrevision': {
            'Meta': {'ordering': "('-revised_at',)", 'object_name': 'PoemRevision'},
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'approximate_publication_date': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'audio_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poems.Poet']"}),
            'body': ('django.db.models.fields.TextField', [], {'default': "'Body'", 'null': 'True', 'blank': 'True'}),
            'display_type': ('django.db.models.fields.CharField', [], {'default': "'poetry'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'longest_line': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'poem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poems.Poem']"}),
            'public_domain': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'revised_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'show_draft_revisions': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_published_revisions': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'source_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'default': "'Title'", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'poems.poet': {
            'Meta': {'object_name': 'Poet'},
            'archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'archive_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deathdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'premium_user': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public_domain': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'wikipedia_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'poems.read': {
            'Meta': {'object_name': 'Read'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poems.Poem']"}),
            'read_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'reader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poems.Poet']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['poems']