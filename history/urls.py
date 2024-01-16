from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import PostDonationRequest, DonationRequestAcceptView
urlpatterns = [
    path('create_request/', PostDonationRequest.as_view(), name='post_request'),
    path('donate_blood/<int:id>/', DonationRequestAcceptView.as_view(), name='donate_blood'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)