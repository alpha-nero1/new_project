from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

## Custom user creation form so we can check
## form validity
##
class UserCreationForm(UserCreationForm):

    email = forms.EmailField()
    user_name = forms.CharField(required=True)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput)
    date_of_birth = forms.DateField(required=True)

    def __init__(self, *args, **kargs):
        super(UserCreationForm, self).__init__(*args,**kargs)

    class Meta:
        model = User

        ## all the fields deeming the form valid
        fields = (
            'user_name',
            'email',
            'password1',
        )

class UserLoginForm(forms.ModelForm):

    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput)

    def __init__(self, *args, **kargs):
        super(UserLoginForm, self).__init__(*args,**kargs)

    ## all the fields deeming the form valid
    class Meta:
        model = User

        fields = (
            'email',
            'password',
        )

