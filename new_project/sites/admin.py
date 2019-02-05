# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Site, DayFeature

# Register your models here.
admin.site.register(Site)
admin.site.register(DayFeature)