# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from authentication.models import User
from sites.models import Site

import uuid


class Folder(models.Model):
    universal_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)  # our hash key
    name = models.CharField(max_length=99)
    # link to library it belongs to
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, default=None)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, default=None)  # ref to user
    # snapshot of path where model created
    created_at = models.CharField(max_length=999999, default='/mylib/')
    sites = models.ManyToManyField(Site)

    def get_return_path(self):
        return '/MyLib/' + str(self.universal_id) + '/'

    def __str__(self):
        return self.name + '/'
