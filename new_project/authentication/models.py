# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .user_manager import User_Manager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _ ## this import is for auto translating
from django.utils import timezone
from datetime import date
from django.contrib import admin

# Create your models here.

## Completely custom user model
## Required for custom authentication
##

class User(AbstractBaseUser, PermissionsMixin):

    # All of our custom fields.
    # blank = False means the field is required.
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(_('user name'), max_length=30, unique=True)
    date_of_birth = models.DateField(_('date of birth'), null=True)
    my_tags = models.CharField(_('my tags'), max_length=255, unique=False, default='')
    image = models.FileField(upload_to='documents/%Y/%m/%d/', null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    start_date = models.DateField(default=timezone.now)

    objects = User_Manager()

    # use email as the username field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.get_full_name()

    def get_short_name(self):  # required
        return self.user_name

    def get_full_name(self):  # required
        return self.user_name

    def get_tag_list(self):
        tags = self.my_tags.split(',')
        self.clean_tags(tags)
        return tags

    ## This is so important
    ## Otherwise the query could match lists containing ' '
    def clean_tags(self, tags):
        if tags:
            if tags[0] == '' or tags[0] == ',':
                del tags[0]

    def format_date(self):
        return self.date_of_birth.strftime('%d/%m/%Y')
