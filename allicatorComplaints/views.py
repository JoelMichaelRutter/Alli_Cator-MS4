"""
1 - Importing render shortcut.
2 - Importing generic view template from django views.
3 - 
"""
from django.shortcuts import render
from django.views import generic
from .models import Complaint

# Create your views here.


class ComplaintList(generic.ListView):
    model = Complaint
