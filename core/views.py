from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactUsForm, ServiceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Models
from .models import Service, ContactUs
from account.models import UserProfile, BloodGroup
from event.models import Event
from history.models import DonationReport
from django.db.models import Q
from django.utils import timezone
#Views
from django.views.generic import ListView, DetailView, CreateView,TemplateView, UpdateView, DeleteView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'donors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blood_group_slug = self.kwargs.get('blood_group_slug')
        donors = UserProfile.objects.all()
        if blood_group_slug:
            blood_group = BloodGroup.objects.get(slug=blood_group_slug)
            donors = UserProfile.objects.filter(blood_group=blood_group)

        if 'search_query' in self.request.GET:
            q = self.request.GET['search_query']
            multiple_q = Q(blood_group__blood_type__icontains=q) | Q(user__first_name__icontains=q) | Q(user__last_name__icontains=q)
            donors = donors.filter(multiple_q)

        context['donors'] = donors
        context['form'] = ContactUsForm()
        context['data'] = Service.objects.all()
        context['blood_group'] = BloodGroup.objects.all()
        context['total_user'] = UserProfile.objects.all().count()
        context['total_donated'] = DonationReport.objects.all().count()
        context['total_available_donor'] = UserProfile.objects.filter(is_available=True).count()
        context['events'] = Event.objects.filter(event_date__gte=timezone.now(), is_approved=True)

        return context
    # For contact Form
    def post(self, request, *args, **kwargs):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message submitted successfully. Thank you.')
            return redirect('homepage')

        return self.render_to_response(self.get_context_data())
    


# User Mini Profile
class UserMiniProfileView(DetailView):
    template_name='mini_profile.html'
    model = UserProfile
    def get_object(self):
        user_id = self.kwargs.get('id')
        return UserProfile.objects.get(pk=user_id)
    
class AboutView(TemplateView):
    template_name = 'about.html'
    
class GuideLineView(TemplateView):
    template_name = 'user_guide.html'

class ServiceDetails(DetailView):
    template_name = "service_detail.html"
    model = Service
    def get_object(self):
        return Service.objects.get(slug=self.kwargs['slug'])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(username='admin')
        return context

# Admin Special
class AddServicesView(CreateView):
    template_name = "services.html"
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request, "Service Added Successfully.")
        return super().form_valid(form)
    

class EditServicesView(UpdateView):
    template_name = "services.html"
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('homepage')
    def get_object(self):
        return Service.objects.get(slug = self.kwargs['slug'])
    def form_valid(self, form):
        messages.success(self.request, "Service Updated Successfully")
        return super().form_valid(form)
    
class DeleteServicesView(DeleteView):
    template_name= 'confirm_delete_service.html'
    model = Service
    success_url = reverse_lazy('homepage')
    def get_object(self):
        return Service.objects.get(slug = self.kwargs['slug'])
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Service deleted successfully.")
        return super().delete(request, *args, **kwargs)

class ContactUsView(ListView):
    model = ContactUs
    template_name = 'contact_us_message.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.all()
        return context
    