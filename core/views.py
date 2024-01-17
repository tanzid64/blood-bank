from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.models import UserProfile, BloodGroup
from django.contrib import messages
from .forms import ContactUsForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from .models import Service, ContactUs
from history.models import DonationReport
from django.db.models import Q
#Views
from django.views.generic import ListView, DetailView, CreateView,TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'donors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blood_group_slug = self.kwargs.get('blood_group_slug')
        if blood_group_slug:
            blood_group = BloodGroup.objects.get(slug=blood_group_slug)
            donors = UserProfile.objects.filter(blood_group=blood_group)
        else:
            donors = UserProfile.objects.all()

        if 'q' in self.request.GET:
            q = self.request.GET['q']
            multiple_q = Q(blood_group__blood_type__icontains=q) | Q(user__first_name__icontains=q) | Q(user__last_name__icontains=q)
            donors = donors.filter(multiple_q)

        context['donors'] = donors
        context['form'] = ContactUsForm()
        context['data'] = Service.objects.all()
        context['blood_group'] = BloodGroup.objects.all()
        context['total_user'] = UserProfile.objects.all().count()
        context['total_donated'] = DonationReport.objects.all().count()
        context['total_available_donor'] = UserProfile.objects.filter(is_available=True).count()

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
