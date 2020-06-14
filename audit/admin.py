from django.contrib import admin
from .models import Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['issue_id', 'title', 'system', 'typ', 'content', 'sender', 'send_time', 'auditors',
                    'audit_time', 'handler', 'handle_time', 'status', 'comment']

