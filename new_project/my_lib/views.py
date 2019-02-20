# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Folder
from sites.models import Site


# view to display folder - includes MyLib
class FolderView(View):
    template_name = "templates/folder.html"

    def get(self, request, universal_id=None):

        folder = folder_check(request, universal_id)

        sub_folders = Folder.objects.filter(parent=folder)

        return render(request, self.template_name, {"folder": folder,
                                                    "sub_folders": sub_folders,
                                                    "sub_sites": folder.sites.all()})


# view to create a folder
class CreateFolder(View):

    def post(self, request, universal_id=None):

        parent_folder = folder_check(request, universal_id)  # this folder

        new_folder = Folder(parent=parent_folder,
                            name=request.POST["folder_name"], user=request.user)
        new_folder.save()

        return redirect(parent_folder.get_return_path())


# view to delete a folder
class DeleteFolder(View):

    def post(self, request, universal_id=None):

        parent_folder = folder_check(request, universal_id)  # this folder

        folder = Folder.objects.get(universal_id=request.POST['folder'])
        folder.delete()

        return redirect(parent_folder.get_return_path())


# view to delete a site from a folder
class DeleteSite(View):

    def post(self, request, universal_id):
        site_id = request.POST["site"]

        folder = Folder.objects.get(universal_id=universal_id)
        this_site = Site.objects.get(id=site_id)

        folder.sites.remove(this_site)
        folder.save()

        return redirect(folder.get_return_path())


def folder_check(request, universal_id):
    folder = None
    if universal_id:
        folder = Folder.objects.get(universal_id=universal_id)
    else:
        folder = Folder.objects.get(name='MyLib', user=request.user)
    return folder
