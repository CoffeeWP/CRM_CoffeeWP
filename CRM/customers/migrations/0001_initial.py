# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'customers_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('tasks', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('contact_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'customers', ['Customer'])

        # Adding model 'Project'
        db.create_table(u'customers_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.Customer'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'customers', ['Project'])

        # Adding model 'Income'
        db.create_table(u'customers_income', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.Project'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('work_time', self.gf('django.db.models.fields.IntegerField')()),
            ('recipe', self.gf('django.db.models.fields.BooleanField')()),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'customers', ['Income'])

        # Adding model 'Outcome'
        db.create_table(u'customers_outcome', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.Project'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'customers', ['Outcome'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'customers_customer')

        # Deleting model 'Project'
        db.delete_table(u'customers_project')

        # Deleting model 'Income'
        db.delete_table(u'customers_income')

        # Deleting model 'Outcome'
        db.delete_table(u'customers_outcome')


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
            'recipe': ('django.db.models.fields.BooleanField', [], {}),
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
