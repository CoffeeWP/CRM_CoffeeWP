# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Income.recipe' to match new field type.
        db.rename_column(u'customers_income', 'recipe', 'receipt')
        # Changing field 'Income.recipe'
        db.alter_column(u'customers_income', 'receipt', self.gf('django.db.models.fields.BooleanField')(db_column='receipt'))

    def backwards(self, orm):

        # Renaming column for 'Income.recipe' to match new field type.
        db.rename_column(u'customers_income', 'receipt', 'recipe')
        # Changing field 'Income.recipe'
        db.alter_column(u'customers_income', 'recipe', self.gf('django.db.models.fields.BooleanField')())

    models = {
        u'customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'contact_date': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tasks': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'customers.income': {
            'Meta': {'object_name': 'Income'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'project_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customers.Project']"}),
            'recipe': ('django.db.models.fields.BooleanField', [], {'db_column': "'receipt'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'work_time': ('django.db.models.fields.IntegerField', [], {})
        },
        u'customers.outcome': {
            'Meta': {'object_name': 'Outcome'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'project_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customers.Project']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'customers.project': {
            'Meta': {'object_name': 'Project'},
            'customer_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customers.Customer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['customers']