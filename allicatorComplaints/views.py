"""
1 - Importing render shortcut.
2 - Importing generic view template from django views.
3 - 
"""
from django.shortcuts import render
from django.views import generic
from .models import Complaint

# Create your views here.


class ViewComplaintList(generic.ListView):
    model = Complaint
    complaint_list = Complaint.objects.filter().order_by('date_logged')
    template_name = 'index.html'
    paginate_by = 10
