from django.urls import path
from .views import *

app_name = 'audit'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', LoginView.as_view(), name='login'),
    path('index/', IndexView.as_view(), name='index'),
    path('create_issue/', CreateIssueView.as_view(), name='create_issue'),
    path('success/', SuccessView.as_view(), name='success'),
    path('logout/', logout, name='logout'),
]
