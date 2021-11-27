"""
1 - Importing path method for use in URL patterns list
2 - Importing all views for use in URL patterns list
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ViewComplaintList.as_view(), name="home"),
    path('add-complaint', views.add_complaint, name='add-complaint'),
    path('edit-complaint/<log_number>/',
         views.edit_complaint,
         name='edit-complaint'
         ),
    path('delete-complaint/<log_number>/',
         views.delete_complaint,
         name='delete-complaint'
         )
]
