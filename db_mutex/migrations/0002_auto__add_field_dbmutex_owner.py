# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DBMutex.owner'
        db.add_column(u'db_mutex_dbmutex', 'owner',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DBMutex.owner'
        db.delete_column(u'db_mutex_dbmutex', 'owner')


    models = {
        u'db_mutex.dbmutex': {
            'Meta': {'object_name': 'DBMutex'},
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lock_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            'owner': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'})
        }
    }

    complete_apps = ['db_mutex']