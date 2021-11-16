"""
IMPORTS
1 - Importing forms from django.
2 - Importing complaint model form models.py
"""
from django.forms import ModelForm
from .models import Complaint


class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = [
            'log_number',
            'customer_surname',
            'complaint_category',
            'date_logged',
            'case_owner',
            'welcome_email',
            'customer_contacted',
            'holding_correspondence',
            'outstanding_actions',
            'latest_update',
            ]
