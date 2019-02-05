from django.forms import ModelForm
from.models import Site
from django.db import models

class Create_Site_Form(ModelForm):
    title = models.CharField(max_length=50)
    tags = models.CharField(max_length=255)
    content = models.CharField(max_length=10000)

    ## all the fields deeming the form valid
    class Meta:
        model = Site

        fields = (
            'title',
            'tags',
            'content',
        )