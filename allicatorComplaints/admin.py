"""
IMPORTS
1 - Imorting admin library
2 - Importing installed django summernote model admin to use
filtering, display and search functionality in Admin site.
3 - Importing export mixin from import export library to
use in ComplaintAdmin class to export data out of application.
4 - Importing fields and resources from import_export library
to use in ComplaintExportResource class.
5 - Importing foregin key widget from import_export library
to access User model to assign username to case_owner rather
than user model primary key.
6 - Importing User model for use in resource class.
7 - Importing Complaint data model
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ExportMixin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User
from .models import Complaint


class ComplaintExportResource(resources.ModelResource):

    class Meta:
        model = Complaint
        fields = (
            'id',
            'log_number',
            'complaint_category',
            'date_logged',
            'case_owner',
            'welcome_email',
            'customer_contacted',
            'holding_correspondence',
            'outstanding_actions',
            'latest_update',
        )
        # Excludes the ID field from being generated on the export.
        exclude = ('id')
        # Reorders the export fields in light of the case_owner foreign key
        # switch to ensure that the report that is generated is in the
        # same order as the system.
        export_order = (
            'log_number',
            'complaint_category',
            'date_logged',
            'case_owner',
            'welcome_email',
            'customer_contacted',
            'holding_correspondence',
            'outstanding_actions',
            'latest_update',
        )
    # On export, the case_owner was being rendered as the User model pk
    # integer. The below code uses the import_export library foreign
    # key widget and replaces the pk with the entries username.
    case_owner = fields.Field(
        column_name='case_owner',
        attribute='case_owner',
        widget=ForeignKeyWidget(User, 'username')
        )


@admin.register(Complaint)
class ComplaintAdmin(ExportMixin, SummernoteModelAdmin):
    list_filter = ('date_logged', 'complaint_category')
    list_display = (
        'log_number',
        'date_logged',
        'customer_surname',
        'complaint_category',
        'case_owner',
        'latest_update'
        )
    search_fields = ['log_number', 'customer_surname']
    resource_class = ComplaintExportResource
