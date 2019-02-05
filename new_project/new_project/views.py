from django.shortcuts import render, redirect
from django.views.generic import View


class BaseRedirect(View):
    def get(self, request):
        return redirect('home:home')
