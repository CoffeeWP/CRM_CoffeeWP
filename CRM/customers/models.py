from pyexpat import model
from django.db import models


class Customer(models.Model):
    name = models.CharField('Name', max_length=70)
    phone_number = models.CharField('Phone Number', max_length=20)
    website = models.URLField('Website Address')
    email = models.EmailField('E-Mail')
    tasks = models.URLField('Tasks')
    contact_date = models.DateTimeField('Contact Data')

    def __unicode__(self):
        return self.name


class Project(models.Model):
    customer_name = models.ForeignKey(Customer)
    name = models.CharField('Name', max_length=70)

    def __unicode__(self):
        return self.name


class Income(models.Model):
    project_name = models.ForeignKey(Project)
    date = models.DateTimeField('Date')
    type = models.CharField('Type', max_length=100)
    value = models.IntegerField('Value')
    work_time = models.IntegerField('Work Time')
    recipe = models.BooleanField('Receipt', db_column='receipt')
    note = models.TextField('Note')

    def __unicode__(self):
        return self.type


class Outcome(models.Model):
    project_name = models.ForeignKey(Project)
    date = models.DateTimeField('Date')
    type = models.CharField('Type', max_length=100)
    value = models.IntegerField('Value')
    note = models.TextField('Note')

    def __unicode__(self):
        return self.type
