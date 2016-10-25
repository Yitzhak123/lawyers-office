
from django.db import models


class Record(models.Model):
    name = models.CharField(max_length=100)


class Lawyer(models.Model):
    name = models.CharField(max_length=30)
    records = models.ManyToManyField(Record)
