from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'login.html'
