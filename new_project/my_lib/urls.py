from django.conf.urls import url, include
from .views import CreateFolder, FolderView, DeleteSite, DeleteFolder

app_name = "my_lib"

urlpatterns = [
    url(r'^(?P<universal_id>[\w|\W]+)/create_folder/', CreateFolder.as_view(), name="create_folder"),
    url(r'^(?P<universal_id>[\w|\W]+)/delete_folder/', DeleteFolder.as_view(), name="delete_folder"),
    url(r'^(?P<universal_id>[\w\W]+)/delete_site/$', DeleteSite.as_view(), name="delete_site"),
    url(r'^delete_site/', DeleteSite.as_view(), name="delete_site_my_lib"),
    url(r'^delete_folder/', DeleteFolder.as_view(), name="delete_folder_my_lib"),
    url(r'^create_folder/', CreateFolder.as_view(), name="create_folder_my_lib"),
    url(r'^$', FolderView.as_view(), name="my_lib"),
    url(r'^(?P<universal_id>[\w|\W]+)/$', FolderView.as_view(), name="view_folder"),
]