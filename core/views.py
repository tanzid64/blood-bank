from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.models import UserProfile, BloodGroup
from django.contrib import messages
from .forms import ContactUsForm
# Models
from .models import Service, ContactUs
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

        context['donors'] = donors
        context['form'] = ContactUsForm()
        context['data'] = Service.objects.all()
        context['blood_group'] = BloodGroup.objects.all()
        context['total_user'] = UserProfile.objects.all().count()
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
