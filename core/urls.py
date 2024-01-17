from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import HomeView, UserMiniProfileView
urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    # path('contact_us/', ContactUsView.as_view(), name='contact_us'),
    path('user_profile/<int:id>/', UserMiniProfileView.as_view(), name='mini_profile'),
    path('blood_group/<slug:blood_group_slug>/', HomeView.as_view(), name='blood_group_wise_post'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)