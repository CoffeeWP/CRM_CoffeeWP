from django.conf.app_template import models
from django.db import models


class Review(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField('Name', max_length=70)
    customer_name = models.ForeignKey('customers.Customer')
    date = models.DateTimeField('Date')
    rate = models.FloatField('Rate')
    note = models.TextField('Note')


class Question(models.Model):
    def __unicode__(self):
        return self.text

    review = models.ForeignKey(Review)
    date = models.DateTimeField('Date')
    text = models.TextField('Text')

