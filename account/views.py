from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView, ListView
from .forms import UserRegistrationForm, UserProfileUpdateForm
from django.contrib import messages
from .constants import send_user_email
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from django.views import View
from django.contrib.auth.views import LogoutView, LoginView
from history.models import DonationReport, DonationRequest
from django.contrib.auth.mixins import LoginRequiredMixin
#Token
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

# Create your views here.
# Registration
class UserRegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    model = User
    success_url = reverse_lazy('register')
    def form_valid(self, form):
        user = form.save()
        print(user)
        token = default_token_generator.make_token(user)
        print("token ", token)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        print("uid ", uid)
        confirm_link = f"https://bindu-blood-bank.onrender.com/accounts/active/{uid}/{token}"
        send_user_email('Account Confirmation Email', confirm_link, 'confirm_email.html', user.email)
        messages.success(self.request, 'User creation successfull, please check your email to active account.')
        return super().form_valid(form)

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
        print(user, token)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, UnicodeDecodeError) as e:
        print(f"Error during activation: {e}")
        user = None
    print(user)
    print(token)
    if user:
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Account Verification Successful. Please update your full profile.')
        return redirect('update_profile') 
    else:
        messages.error(request, 'Invalid activation link. Please register again.')
        return redirect('register')

# Login and Logout
class UserLoginView(LoginView):
    template_name = 'login.html'

def UserLogoutView(request):
    logout(request)
    return redirect('homepage')

# update or edit profile
class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile_update.html'
    form_class = UserProfileUpdateForm
    success_url = reverse_lazy('profile')
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile Updated Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Information Incorrect')
        return super().form_invalid(form)

# Details Profile
class UserProfileView(LoginRequiredMixin, ListView):
    template_name='profile.html'
    model = DonationReport
    def get_object(self):
        return DonationReport.objects.filter(profile = self.request.user.profile)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user.profile
        context["user"] = user
        context["events"] = DonationRequest.objects.filter(created_by = user)
        return context
    

