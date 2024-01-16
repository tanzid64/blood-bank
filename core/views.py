from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView
from account.models import UserProfile, BloodGroup
# Models
from .models import Service
#Views
from django.views.generic import ListView
# Create your views here.
def home(request):
    return render(request, 'home.html')

class HomeView(ListView):
    model = Service
    template_name = 'home.html'
    context_object_name = 'donors'

    def get_queryset(self):
        blood_group_slug = self.kwargs.get('blood_group_slug')
        if blood_group_slug:
            blood_group = BloodGroup.objects.get(slug=blood_group_slug)
            return UserProfile.objects.filter(blood_group=blood_group)
        return UserProfile.objects.all()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['data'] = Service.objects.all()
        context['blood_group'] = BloodGroup.objects.all()
        context['total_user'] = UserProfile.objects.all().count()
        context['total_available_donor'] = UserProfile.objects.filter(is_available=True).count()
        print(context['total_available_donor'])
        return context

class UserMiniProfileView(DetailView):
    template_name='mini_profile.html'
    model = UserProfile
    def get_object(self):
        user_id = self.kwargs.get('id')
        return UserProfile.objects.get(pk=user_id)
