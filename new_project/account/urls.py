from django.conf.urls import url
from .views import Account, ImageUpload, Tags

app_name = 'account'

urlpatterns = [
    url(r'^$', Account.as_view(), name="account"),
    url(r'^image_upload', ImageUpload.as_view(), name="image_upload"),
    url(r'^tags', Tags.as_view(), name="tags"),
]