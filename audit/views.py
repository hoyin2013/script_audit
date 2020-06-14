import time

from django.contrib.auth.models import Group
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from audit.forms import IssueForm
from audit.models import Issue


class LoginView(TemplateView):
    template_name = 'login.html'


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            current_user_set = self.request.user
            # 获取用户的组名
            current_group_set = str(Group.objects.get(user=current_user_set))

            # print(type(current_group_set))

            if current_group_set == 'DBA':
                # print("I am DBA")
                issue_lists = Issue.objects.all()
                # print(issue_lists)
            elif current_group_set == 'DEV':
                issue_lists = Issue.objects.filter(~Q(sender=current_user_set))
            elif current_group_set == 'AUDIT':
                issue_lists = Issue.objects.filter(~Q(auditors=current_user_set))
            # print(issue_lists)

            issue_id = str(current_user_set) + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

            context['issue_lists'] = issue_lists
            context['group'] = current_group_set
            context['issue_id'] = issue_id
            # print(context)
            return context


class CreateIssueView(LoginRequiredMixin, CreateView):
    form_class = IssueForm
    template_name = 'issue_add.html'
    success_url = '/success'


class SuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'success.html'

