
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


class Case(models.Model):
    who = models.CharField(max_length=30)
    about = models.CharField(max_length=30)
    owner = models.ForeignKey(User)

    def __str__(self):
        return '[who = '+str(self.who)+', about = '+str(self.about)+']'


class Office(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return '[name = '+str(self.name)+']'


class Lawyer(models.Model):
    username = models.CharField(max_length=30, null=True, unique=True,
                                error_messages={'unique': "This username already exist"})
    email = models.EmailField(max_length=60, null=True, unique=True,
                              error_messages={'unique': "This email already exist"})
    password = models.CharField(max_length=20, null=True)
    cases = models.ManyToManyField(Case)
    office = models.ForeignKey(Office)

    def add_new_lawyer(self, office='o1'):
        try:
            office = Office.objects.get(name=office)
        except:
            office = Office.objects.get(name='o1')

        User.objects.create_user(username=self.username, email=self.email,
                                 password=self.password)
        self.password = User.objects.get(username=self.username).password
        self.office_id = office.id
        self.save()

    def add_new_case(self, case):
        self.cases.add(case)

    def __str__(self):
        return '[name = '+str(self.username)+']'


# class LawyerManager(Lawyer):

# This Model is for internal use
class Link(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    active = models.BooleanField(default=False)

    def __str__(self):
        return "name = "+self.name+", url = "+self.url+\
               ", active = "+str(self.active)


class SelectBox(models.Model):
    name = models.CharField(max_length=50)


class Option(models.Model):
    value = models.CharField(max_length=50)
    select_box = models.ForeignKey(SelectBox)