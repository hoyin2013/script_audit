# coding:utf-8
from datetime import datetime

from django import forms
from audit.models import Issue


class IssueForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            # self.fields['sender'].widget.attrs['readonly'] = True
            # self.fields['sender'].initial = '张三'
            # self.fields['auditors'].widget = forms.CheckboxSelectMultiple()

    # issue_id = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Issue
        # issue_id 自动生成 用户+时间戳+数列
        fields = [
            # 'issue_id', 'title', 'system', 'typ', 'content', 'sender', 'auditors'
            'issue_id', 'title', 'system', 'typ', 'content', 'sender', 'auditors', 'status'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=50, required=True)
