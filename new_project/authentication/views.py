from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import auth ## access auth module
from .user_backend import User_Backend
from .forms import UserCreationForm, UserLoginForm
from my_lib.models import Folder

class Auth(View):

    auth_class = User_Backend()

    ## Common authentication check method.
    def user_check(self, request, email, password):
        user = self.auth_class.authenticate(username=email, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return True
        return False


# Create your views here.
class Login(Auth):

    form_class = UserLoginForm
    template_name = "templates/login.html"

    def get(self, request):
        return render(request, self.template_name, None)

    def post(self, request):
        form = self.form_class(request.POST)

        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        auth_fail = None

        ## just so we can send back errors
        if form.is_valid():
            print()

        if self.user_check(request, email, password):
            return redirect('home:home')

        if email and password:
            auth_fail = True

        print(form.errors)

        ## I really don't like that the user is just sent back, find a workaround!
        return render(request, self.template_name, {'user': request.user, 'form': form, 'old_email': email, 'auth_error': auth_fail})


class Sign_Up(Auth):

    form_class = UserCreationForm
    template_name = "templates/sign_up.html"

    def get(self, request):
        return render(request, self.template_name, None)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # not saved permanently in db yet

            ## clean normalised data.
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            ## password setting.
            user.set_password(password)

            ## register user.
            user.save()

            ## create the users MyLib
            my_lib = Folder(parent=None, user=user, name='MyLib')
            my_lib.save()

            if self.user_check(request, email, password):
                return redirect('home:home')

                ## we send back the form so we can do things with the errors
                ## we also send back the old data so user doesnt need to keep filling fields.
        return render(request, self.template_name, {'form': form, 'old_data': request.POST})


class Log_Out(View):

    def get(self, request):
        auth.logout(request)
        return redirect('authentication:login')