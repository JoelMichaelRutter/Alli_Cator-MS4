# WORK IN PROGRESS AS BACK UP IF CANT GET FORM WORKING WITHOUT FORMS.PY FILE

from django import forms
from .models import Complaint


class AddComplaintForm(forms.ModelForm):
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
            'latest_update'
            ]

        widgets = {
            'log_number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date_logged': forms.DateTimeInput(attrs={
                'class': 'form-control'
            }),
        }
        #     'customer_surname': forms.TextInput(attrs={
        #         'class': 'form-control'
        #     }),
        #     'complaint_category': forms.TextInput(attrs={
        #         'class': 'form-control'
        #     }),
        #
        #     'date_logged': forms.DateTimeInput(attrs={
        #         'class': 'form-control'
        #     }),