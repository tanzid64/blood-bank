from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import DonationRequest, DonationReport
from django.views.generic import ListView, CreateView, UpdateView
from django.views import View
from django.contrib import messages
from datetime import datetime
from django.shortcuts import get_object_or_404
from .forms import EditDonationRequestForm
from django.db.models import Q
# Create your views here.
# Create a Request
class PostDonationRequest(CreateView):
    template_name='post_donation.html'
    model = DonationRequest
    form_class = EditDonationRequestForm
    success_url = reverse_lazy('dashboard')
    def form_valid(self, form):
        form.instance.created_by = self.request.user.profile
        messages.success(self.request, 'Request added successfully.')
        return super().form_valid(form)

class EditDonationRequest(UpdateView):
    template_name = 'post_donation.html'
    form_class = EditDonationRequestForm
    success_url = reverse_lazy('dashboard')
    model = DonationRequest
    def form_valid(self, form):
        messages.success(self.request, 'Post edited successfully.')
        return super().form_valid(form)


class DashboardView(ListView):
    template_name = 'dashboard.html'
    model = DonationRequest
    context_object_name = 'events'

    def get_queryset(self):
        queryset = DonationRequest.objects.filter(is_accepted=False)

        if 'q' in self.request.GET:
            search_term = self.request.GET['q']
            queryset = queryset.filter(
                Q(created_by__user__first_name__icontains=search_term) |
                Q(created_by__user__last_name__icontains=search_term) |
                Q(blood_group__blood_type__icontains=search_term) |
                Q(location__icontains=search_term) |
                Q(description__icontains=search_term)
            )

        return queryset


class DonationRequestAcceptView(View):
    def get(self, request, id):
        event = DonationRequest.objects.get(pk=id)
        donor = self.request.user.profile

        if event.blood_group == donor.blood_group:
            if donor.is_available:
                # Updating Donetion Request
                event.is_accepted = True
                event.save()
                # Updating User Profile
                donor.total_donated += 1
                donor.last_donation_date = datetime.now().date()
                donor.save()
                # Updating User History or Donation Report
                report = DonationReport(profile=donor, event = event)
                report.save()
                messages.success(self.request, 'Donation Successfull. Thanks for your help.')
            else:
                messages.warning(self.request, 'You cannot donate blood now, you have to wait at least three months from your previous donation date.')
        else:
            messages.error(self.request, "Only same blood group's user can donate.")
        
        return redirect('dashboard')

class ManagedOfflineView(View):
    def get(self, request, id):
        event = DonationRequest.objects.get(pk=id)
        event.is_accepted = True
        event.save()
        messages.success(self.request, 'Blood managed in offline.')
        return redirect('dashboard')


        
