from django.contrib import admin
from .models import Service, ContactUs
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug']
admin.site.register(Service, ServiceAdmin)
admin.site.register(ContactUs)