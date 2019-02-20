""" Import relevant django modules. """
from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Q
""" Import written modules. """
from my_lib.models import Folder
from .forms import Create_Site_Form
from .models import Site, Comment


class CreateSite(View):
    template_name = "templates/new_site.html"

    def get(self, request):
        return render(request, self.template_name, None)

    def post(self, request):
        form = Create_Site_Form(request.POST)

        if form.is_valid():
            site = form.save(commit=False)  # not saved permanently in db yet
            site.owner_id = request.user
            site.save()

        return redirect('home:home')


class ViewSite(View):
    template_name = 'templates/site.html'

    def get(self, request, id):
        site = Site.objects.get(id=id)
        folders = Folder.objects.filter(
            user=request.user)  ## send folders through for selection
        return render(request, self.template_name, {
            "site": site,
            "folders": folders
        })

    def post(self, request,
             id):  ## post reserved for votes I DO NOT LIKE THIS.
        amount = int(request.POST["amount"])
        site = Site.objects.get(id=id)
        comments = Comment.objects.filter(Q(site=site))
        site.votes = site.votes + amount
        site.save()

        return render(request, 'templates/votes.html', {
            "votes": site.votes,
            "comments": comments
        })


class SearchSites(View):
    template_name = 'templates/components/search_results.html'

    def post(self, request):
        if not (request.POST['search_key']):
            return redirect('home:home')

        search_key = request.POST['search_key']
        sites = Site.objects.filter(Q(title__icontains=search_key))

        return render(request, self.template_name, {'sites': sites})


## class handling site comments (accessed via ajax only)
class CommentView(View):
    template_name = "templates/components/comments.html"

    ## note: this post is to render only segment of the page
    ## and not reload the page entirely.
    def post(self, request, id):
        comment = request.POST['comment']

        site = Site.objects.get(id=id)  # i don't love this..

        # for readability; keep this format of object creation
        comment = Comment(owner=request.user, text=comment, site=site)
        comment.save()
        comments_arr = Comment.objects.filter(site=site)

        return render(request, self.template_name, {'comments': comments_arr})


class SaveSite(View):
    def post(self, request, id):
        folder_name = request.POST["folder"]
        folder = Folder.objects.get(
            user=request.user, name=folder_name)  # get users lib object
        site = Site.objects.get(id=id)

        folder.sites.add(site)
        folder.save()

        return redirect(folder.get_return_path())
