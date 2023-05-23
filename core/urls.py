from django.urls import re_path, path, include

from core import views

urlpatterns = [
    re_path(r'^$', views.Home.as_view(), name='home'),
]
