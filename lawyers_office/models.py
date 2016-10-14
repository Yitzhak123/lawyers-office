from django.db import models
from django.utils import timezone


class Record(models.Model):
    who = models.CharField(max_length=30)
    about = models.CharField(max_length=30)

    def __str__(self):
        return '[who = '+str(self.who)+', about = '+str(self.about)+']'


class Office(models.Model):
    name = models.CharField(max_length=40)


class Lawyer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, null=True)
    password = models.CharField(max_length=20, null=True)
    records = models.ManyToManyField(Record)
    office = models.ForeignKey(Office)

    def __str__(self):
        return '[name = '+str(self.name)+']'

