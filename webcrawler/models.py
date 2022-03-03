
from django.contrib import admin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
# Create your models here.


class Url_crawler_list(models.Model):
    url = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url


class Url_freejobalert(models.Model):
    url = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


class Url_sarkariresult(models.Model):
    url = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


class Url_crawler_other(models.Model):
    url = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


class Url_others(models.Model):
    url = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


class Url_pdf(models.Model):
    url = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url


class Url_home(models.Model):
    url = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=125, blank=True, null=True)
    blacklist = models.BooleanField(default=False)

    def __str__(self):
        return self.url


class Url_Monitor(models.Model):
    url_home = ForeignKey(Url_home, on_delete=CASCADE)
    url_monitor = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url_monitor


class Url_blacklist(models.Model):
    url_blacklist = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url_blacklist
