from django import forms
from .models import DonationRequest
class EditDonationRequestForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['blood_group', 'location', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # For other all fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'block p-2.5 w-full text-sm rounded-lg border bg-gray-700 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500'
                )
            })
        
