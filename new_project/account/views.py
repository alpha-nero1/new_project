## Author: Alessandro Alberga
## Purpose - support account app functionality

from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.db.models import Q
from sites.models import Site

class Account(View):
    template_name = "templates/account.html"

    def get(self, request):
        my_sites = Site.objects.filter(Q(owner_id=request.user))
        tags = request.user.my_tags
        tags_arr = tags.split(',')

        return render(request, self.template_name, {'my_sites': my_sites, 'tags': tags_arr})


    ## return how many times this user has had their sites featured, wouldve prefered in user
    ## class but causes dependency loop
    def get_featured(self, owner):
        return (Site.objects.filter(owner_id=owner, is_featured=True)).count


class ImageUpload(View):

    def post(self, request):
        if request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            request.user.image = uploaded_file_url
            request.user.save()

            return redirect('account:account')

        return redirect('account:account')


## This needs to be its own view, was previously only purpose of account view
##
class Tags(View):
    template_name = "templates/components/tags.html"

    def post(self, request):
        print(request.POST)
        tags = request.POST.get("tags[]").split(',')

        for tag in tags:
            if tag not in request.user.my_tags:
                request.user.my_tags += ("," + tag)

        tags = request.user.get_tag_list
        request.user.save()

        return render(request, 'templates/components/tags.html', {'tags':tags})

