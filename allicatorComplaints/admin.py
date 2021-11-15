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
