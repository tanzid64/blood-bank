from django.contrib import admin
from .models import BloodGroup, UserProfile
# Register your models here.
admin.site.register(BloodGroup)
admin.site.register(UserProfile)