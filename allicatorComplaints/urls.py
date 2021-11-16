"""
1 -
2 -
3 -
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ViewComplaintList.as_view(), name="home"),
]
