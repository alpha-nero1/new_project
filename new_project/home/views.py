from django.shortcuts import render, redirect
from django.views.generic import View
from sites.models import Site
from django.db.models import Q
import operator
import functools
from sites.models import DayFeature
from .models import ThemeImage
from random import randint
from django.db.models.aggregates import Count
from datetime import datetime
from my_lib.models import Folder

class Home(View):
    template_name = "templates/home.html"

    def get(self, request):
        ## initially 'None' because we check later if they exist (need assignment)
        trending = None
        recommendations = None

        ## So an un authorised user can't access site
        if request.user.id == None: return redirect('authentication:login')

        new = self.is_new(request.user)
        todays_feature = DayFeature.objects.all()
        my_lib = Folder.objects.get(user=request.user, name='MyLib', parent=None)

        if todays_feature:
            todays_feature = todays_feature[todays_feature.count() - 1] ## causes neg indexing if none exist

        if Site.objects.all():
            trending = Site.objects.annotate(Count('votes')).order_by('-votes')[:20]
            recommendations = self.recommend(request)

        ## make a callable specific to mobile, we don't need to give them the html data
        return render(request, self.template_name, {'trending': trending,
                                                    'todays_feature': todays_feature,
                                                    'new': new,
                                                    'recommendations': recommendations,
                                                    'my_lib': my_lib })

    def rand(self, objects):
        count = objects.count()
        rand_index = randint(0, count - 1)
        pick = objects.all()[rand_index]
        return pick

    def is_new(self, user):
        yes = False
        if user.start_date == datetime.today():
            yes = True
        return yes

    def recommend(self, request):
        tags = request.user.get_tag_list()

        if tags:
            user = request.user
            user.clean_tags(tags)
            query = functools.reduce(operator.or_, [Q(tags__icontains=str(tag)) for tag in tags])
            return Site.objects.filter(query).order_by('-votes')[:10]

