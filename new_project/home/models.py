# Author: Alessandro Alberga
# This models file is purposed to provide generic data structures for site operation
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import datetime

class ThemeImage(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='documents/%Y/%m/%d/', blank=True)

    ## briliant, now object displays are actually descriptive!
    def __str__(self):
        return self.description





