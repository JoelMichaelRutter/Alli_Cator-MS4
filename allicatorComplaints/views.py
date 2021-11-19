"""
1 - Importing render shortcut and redirect shortcut
2 - Importing generic view template from django views.
3 -
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Complaint
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ViewComplaintList(LoginRequiredMixin, generic.ListView):
    model = Complaint
    def get_queryset(self):
        return Complaint.objects.filter(case_owner=self.request.user).order_by('date_logged')
    template_name = 'index.html'
    paginate_by = 10


def add_complaint(request):
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
        return redirect('home')
    return render(request, 'add_complaint.html')


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
        complaint.holding_correspondence = 'holding_correspondence' in request.POST
        complaint.outstanding_actions = 'outstanding_actions' in request.POST
        complaint.latest_update = request.POST.get('latest_update')
        complaint.save(update_fields=None)
        return redirect('home')
    context = {
        'complaint': complaint,
    }
    return render(request, 'edit_complaint.html', context)


def delete_complaint(request, log_number):
    complaint = get_object_or_404(Complaint, log_number=log_number)
    complaint.delete()
    # context = {
    #     'complaint'
    # }
    return redirect('home')
