"""
IMPORTS
1 - Imorting admin library
2 - Importing installed django summernote model admin
3 - Importing complaint data model
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Complaint


# Register your models here.


@admin.register(Complaint)
class ComplaintAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('log_number',)}
    list_filter = ('date_logged', 'complaint_category')
    list_display = (
        'log_number',
        'date_logged',
        'customer_surname',
        'complaint_category',
        'case_owner'
        )
    search_fields = ['log_number', 'customer_surname']
