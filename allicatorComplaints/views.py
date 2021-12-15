"""
1 - Importing render shortcut and redirect and get_object_or_404 shortcuts
2 - Importing generic view template from django views.
3 - Importing LoginRequiredMixin to ensure that all
users attempting to access the ViewComplaintList view are
redirected to the sign in page to prevent unauthorised access.
4 - Imporing login required decorator for use on function based views.
5 - Importing messages to use in data handling views to provide
custom messages upon user actions.
6 - Importing integrity error module to use in add_complaint view.
7 - Importing Complaint model for use in data handling views.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .models import Complaint

"""
ViewComplaintList
- This view handles the R of the application's CRUD functionality
- The below view parses the database for all of the Complaint objects.
- Inside the view, a custom function filters the entries by the
logged in user making the request so that the user can only see and
manage their own entries.
- The entries are also ordered oldest to newest.
- If there are more than 10 entries for the user, the page is paginated.
"""


class ViewComplaintList(LoginRequiredMixin, generic.ListView):
    model = Complaint

    # This below function overides the default
    # get_queryset function of the ListView class
    # and allows for the custom filter to be applied.
    def get_queryset(self):
        return Complaint.objects.filter(
            case_owner=self.request.user
            ).order_by('date_logged')
    template_name = 'index.html'
    paginate_by = 10


"""
add_complaint
- This view handles the C of the application's CRUD functionality.
- The view is decorated by the @login_required decorator to ensure
that no unauthorised users can access it.
- The request method is checked and if it is "POST",
the view assigns the data from the fields in the add_complaint.html form
to variables of the same name.
- From there, an object within the database is created with the data from
the form.
"""


@login_required
def add_complaint(request):
    try:
        if request.method == 'POST':
            log_number = request.POST.get('log_number')
            customer_surname = request.POST.get('customer_surname')
            complaint_category = request.POST.get('complaint_category')
            date_logged = request.POST.get('date_logged')
            case_owner = request.user
            welcome_email = 'welcome_email' in request.POST
            customer_contacted = 'customer_contacted' in request.POST
            holding_correspondence = 'holding_correspondence' in request.POST
            outstanding_actions = 'outstanding_actions' in request.POST
            latest_update = request.POST.get('latest_update')
            Complaint.objects.create(
                log_number=log_number,
                customer_surname=customer_surname,
                complaint_category=complaint_category,
                date_logged=date_logged,
                case_owner=case_owner,
                welcome_email=welcome_email,
                customer_contacted=customer_contacted,
                holding_correspondence=holding_correspondence,
                outstanding_actions=outstanding_actions,
                latest_update=latest_update,
            )
            messages.success(
                request,
                """Triumphant fanfare! - Complaint
                 successfully added to allocation."""
                )
            return redirect('home')
    except IntegrityError:
        messages.error(
            request,
            """:( Looks like the complaint you're
            trying to add already exists in our records, please try again!"""
        )
        return redirect('home')
    return render(request, 'add_complaint.html')


"""
edit_complaint
- This view handles the U of the application's CRUD functionality.
- The view is decorated by the @login_required decorator to ensure
that no unauthorised users can access it.
- The request and the log_number of the complaint are passed into the function.
- A call to the Complaint data model is invoked and the view will return the
edit_complaint.html template provided a record exists in the db with
that log_number.
- There is a form within the edit_complaint template, and the complaint
that has been found
is passed into the template via the context variable. From there, the
current data for the record is added into the form fields via the various value
html attributes. The user can then change the values via the form.
- In terms of the boolean fields on the model, there is some template logic
contained on the page which assesses the value and renders either a checked
or unchecked Bootstrap switch based on the truthy/falsy value in the db.
- Once the user submits the form, the record is saved. Inside this database
action, the update_fields=None parameter is passed in.
This negates any checking of unchanged database values and the complaint is
overwritten.
- A custom message is passed back to the index.html template upon a successful
submission.
"""


@login_required
def edit_complaint(request, log_number):
    complaint = get_object_or_404(Complaint, log_number=log_number)
    if request.method == 'POST':
        complaint.log_number = request.POST.get('log_number')
        complaint.customer_surname = request.POST.get('customer_surname')
        complaint.complaint_category = request.POST.get('complaint_category')
        complaint.date_logged = request.POST.get('date_logged')
        complaint.case_owner = request.user
        complaint.welcome_email = 'welcome_email' in request.POST
        complaint.customer_contacted = 'customer_contacted' in request.POST
        complaint.holding_correspondence = (
            'holding_correspondence' in request.POST
            )
        complaint.outstanding_actions = 'outstanding_actions' in request.POST
        complaint.latest_update = request.POST.get('latest_update')
        complaint.save(update_fields=None)
        messages.success(request, "Complaint edited successfully.")
        return redirect('home')
    context = {
        'complaint': complaint,
    }
    return render(request, 'edit_complaint.html', context)


"""
delete_complaint
- This view handles the D of the application's CRUD functionality.
- The view is decorated by the @login_required decorator to ensure
that no unauthorised users can access it.
- It is similar in function to the edit complaint view.
- The database is parsed for an entry with a matching log number.
- From there, that entry is deleted.
- A custom message is generated before the redirect back to the index.html
template is invoked using the error message styling.
"""

@login_required
def delete_complaint(request, log_number):
    complaint = get_object_or_404(Complaint, log_number=log_number)
    complaint.delete()
    messages.error(
        request,
        "Chomp chomp! - The complaint has been fed to the Alli_cator."
        )
    return redirect('home')
