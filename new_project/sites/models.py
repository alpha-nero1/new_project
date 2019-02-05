## Author: Alessandro Alberga
##

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from authentication.models import User
from django.utils import timezone
from home.models import ThemeImage
from django.conf import settings
import uuid


class Site(models.Model):
    title = models.CharField(max_length=50)
    tags = models.CharField(max_length=255)
    content = models.CharField(max_length=1000000)
    votes = models.IntegerField(default=0)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE) # reference to owner, bad name its not actually an id
    time_stamp = models.DateTimeField(default=timezone.now)
    site_image = models.ForeignKey(ThemeImage, on_delete=models.CASCADE, null=True, default=None)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_tag_list(self):
        return self.tags.split(',')

    ## formats top 3 tags for view
    def get_cleaned_tags(self):
        tags = self.get_tag_list()[:3]
        tag_str = ""

        for tag in tags:
            tag_str += tag + ", "

        tag_str = tag_str[:-2] ## deletes the , at the end

        return tag_str

    def delete_check(self):
        if (self.vote < -20):
            self.delete()

    def get_comments(self):
        return Comment.objects.filter(site=self)

    ## Bel
    def get_url(self):
        return ("/sites/" + str(self.id) + "/")


## common functionalities for a writeable object i.e comment or reply
class Write_Object(models.Model):
    text = models.CharField(max_length=255)
    time_stamp = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    votes = models.IntegerField(default=0)

    def check_user(self, user):
        if self.owner == user:
            return True

    def delete(self):
        self.delete()

    ## this specific class meta is necessary if we want to
    ## subclass further
    class Meta:
        abstract = True


class Comment(Write_Object):
    site = models.ForeignKey(Site, on_delete=models.CASCADE) # reference to owner


class Reply(Write_Object):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE) # reference to owner


class DayFeature(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=None)
    sub_text = models.CharField(max_length=255)
    time_stamp = models.DateTimeField(default=timezone.now)

    ## this way we know what sites have been featured
    #def __init__(self):
    #    self.site.is_featured = True