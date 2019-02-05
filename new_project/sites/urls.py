from django.conf.urls import url, include
from django.contrib import admin
from .views import Create_Site, View_Site, Comment_View, Save_Site

app_name = "sites"

urlpatterns = [
    url(r'^create_new/', Create_Site.as_view(), name="create_site"),
    url(r'^(?P<id>[\w\-]+)/$', View_Site.as_view(), name="view_site"),
    url(r'^(?P<id>[\w\-]+)/new_comment/$', Comment_View.as_view(), name="comment"),
    url(r'^(?P<id>[\w\-]+)/save_site/$', Save_Site.as_view(), name="save"),
]