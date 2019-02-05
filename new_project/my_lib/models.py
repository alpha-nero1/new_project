# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from authentication.models import User
from sites.models import Site

import uuid

class Folder(models.Model):
    universal_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) ## our hash key
    name = models.CharField(max_length=99)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, default=None) ## link to library it belongs to
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None) ## ref to user
    created_at = models.CharField(max_length=999999, default ='/mylib/') ## snapshot of path where model created
    sites = models.ManyToManyField(Site)

    def get_return_path(self):
        return '/MyLib/' + unicode(self.universal_id) + '/'

    def __str__(self):
        return self.created_at + self.name + '/'
