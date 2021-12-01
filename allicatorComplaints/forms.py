from django import forms
from .models import Complaint


class ComplaintForm(forms.ModelForm):
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
            'latest_update '
        ]
