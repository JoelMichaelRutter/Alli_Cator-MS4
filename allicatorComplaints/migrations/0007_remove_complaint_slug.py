# Generated by Django 3.2.9 on 2021-11-27 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allicatorComplaints', '0006_alter_complaint_latest_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='slug',
        ),
    ]
