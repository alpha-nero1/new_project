from django.conf.urls import url, include
from django.contrib import admin
from .views import Home
from sites.views import SearchSites

app_name = "home"

urlpatterns = [
    url(r'^$', Home.as_view(), name="home"),
    url(r'^search/', SearchSites.as_view(), name="search"),
]