from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import ContactUs, Service
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'image', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # For other all fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'my-3 block p-2.5 w-full text-sm rounded-lg border bg-gray-700 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500'
                )
            })