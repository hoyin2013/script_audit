from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView


class LoginView(TemplateView):
    template_name = 'login.html'
