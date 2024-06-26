from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import PostDonationRequest, DonationRequestAcceptView, EditDonationRequest, ManagedOfflineView
urlpatterns = [
    path('create_request/', PostDonationRequest.as_view(), name='post_request'),
    path('update_request/<int:pk>/', EditDonationRequest.as_view(), name='post_update'),
    path('donate_blood/<int:id>/', DonationRequestAcceptView.as_view(), name='donate_blood'),
    path('mark_as_managed/<int:id>/', ManagedOfflineView.as_view(), name='managed_offline'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)