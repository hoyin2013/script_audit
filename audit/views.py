import time

from django.contrib.auth.models import Group, Permission, User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from audit.forms import IssueForm, LoginForm
from audit.models import Issue
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
import logging

logger = logging.getLogger('__name__')


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_field_name = 'next'
    success_url = '/index/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            request = self.request
            auth_login(request, user)
            print(user)
            return HttpResponseRedirect('/index/')

        return super().form_valid(form)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            current_user_set = self.request.user
            # 获取用户的组名
            current_group_set = str(Group.objects.get(user=current_user_set))

            print(type(current_group_set), current_group_set)
            print(type(current_user_set), current_user_set)

            if str(current_user_set) == 'wangjd':
                issue_lists = Issue.objects.filter(~Q(status=1) & ~Q(status=2))
            elif current_group_set == 'DBA':
                # print("I am DBA")
                issue_lists = Issue.objects.all()
                # print(issue_lists)
            elif current_group_set == 'DEV':
                issue_lists = Issue.objects.filter(Q(sender=current_user_set))
            elif current_group_set == 'AUDIT':
                issue_lists = Issue.objects.filter(Q(auditors=current_user_set))
            # print(issue_lists)

            context['issue_lists'] = issue_lists
            context['group'] = current_group_set

            # print(context)
            return context


class CreateIssueView(LoginRequiredMixin, CreateView):
    form_class = IssueForm
    template_name = 'issue_add.html'
    success_url = '/success'

    def get_context_data(self, **kwargs):
        context = {}
        # 自动生成单号
        issue_id = str(self.request.user) + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        context['issue_id'] = issue_id

        auditors = User.objects.filter(groups__name='AUDIT')

        ads = [ad.username for ad in auditors]
        # print(ads)
        context['ads'] = ads
        context.update(kwargs)
        return super().get_context_data(**context)


class SuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'success.html'


class AuditView(LoginRequiredMixin, View):
    pass
