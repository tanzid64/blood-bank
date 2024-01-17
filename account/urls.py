from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import UserRegistrationView, activate, UserLogoutView, UserLoginView, UserProfileView, UserProfileUpdateView
from history.views import DashboardView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView, name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('update_profile/', UserProfileUpdateView.as_view(), name='update_profile'),
    path('active/<str:uid64>/<str:token>/', activate, name='activate'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)