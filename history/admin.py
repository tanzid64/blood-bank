from django.contrib import admin
from .models import DonationReport, DonationRequest
# Register your models here.
admin.site.register(DonationRequest)
admin.site.register(DonationReport)