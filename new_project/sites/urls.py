from django.conf.urls import url
from .views import CreateSite, ViewSite, CommentView, SaveSite

app_name = "sites"

urlpatterns = [
    url(r'^create_new/', CreateSite.as_view(), name="create_site"),
    url(r'^(?P<id>[\w\-]+)/$', ViewSite.as_view(), name="view_site"),
    url(r'^(?P<id>[\w\-]+)/new_comment/$',
        CommentView.as_view(),
        name="comment"),
    url(r'^(?P<id>[\w\-]+)/save_site/$', SaveSite.as_view(), name="save"),
]