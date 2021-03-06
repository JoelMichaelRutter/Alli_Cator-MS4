"""
- Importing models for us in data model.
- Importing user for use in Complaints model.
"""
from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    """
    - Below is the data model for each complaint that gets logged
      into the system.
    """
    log_number = models.CharField(
      max_length=10,
      unique=True,
      null=False,
      blank=False
    )
    customer_surname = models.CharField(max_length=40, null=False, blank=False)
    complaint_category = models.CharField(
      max_length=100,
      null=False,
      blank=False
    )
    date_logged = models.DateField()
    case_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    welcome_email = models.BooleanField(null=False, blank=False)
    customer_contacted = models.BooleanField(null=False, blank=False)
    holding_correspondence = models.BooleanField(null=False, blank=False)
    outstanding_actions = models.BooleanField(null=False, blank=False)
    latest_update = models.TextField(
      max_length=250,
      unique=False,
      null=False,
      blank=False
    )

    class Meta:
        """
        - Orders complaints in the table oldest to newest.
        """
        ordering = ['date_logged']

    def __str__(self):
        return str(self.log_number)
