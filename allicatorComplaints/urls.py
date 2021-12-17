"""
1 - Importing path method for use in URL patterns list
2 - Importing all views for use in URL patterns list
"""
from django.urls import path
from . import views

# 1 - First URL pattern is for the home screen and connects to
# ViewComplaintList view.

# 2- Second URL pattern connects to the add_complaint view.

# 3 - Third URL pattern connects to the edit_complaint view and
# takes the compaint log number.

# 4 - Fourth URL pattern connects to the delete_complaint view.

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
