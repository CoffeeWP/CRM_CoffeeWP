# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Review'
        db.create_table(u'reviews_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('customer_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.Customer'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('rate', self.gf('django.db.models.fields.FloatField')()),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'reviews', ['Review'])

        # Adding model 'Question'
        db.create_table(u'reviews_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('review', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reviews.Review'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'reviews', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Review'
        db.delete_table(u'reviews_review')

        # Deleting model 'Question'
        db.delete_table(u'reviews_question')


    models = {
        u'customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'contact_date': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'reviews.question': {
            'Meta': {'object_name': 'Question'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reviews.Review']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'reviews.review': {
            'Meta': {'object_name': 'Review'},
            'customer_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customers.Customer']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'rate': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['reviews']