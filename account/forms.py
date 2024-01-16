from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, BloodGroup
from .constants import GENDER_TYPE, BLOOD_GROUP
# Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'required':True}))
    blood_group = forms.ModelChoiceField(queryset=BloodGroup.objects.all(), empty_label=None)
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    # For Unique Email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
    # For Activation by default it should be deactivated
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
            profile, created = UserProfile.objects.get_or_create(user=user, blood_group = self.cleaned_data['blood_group'])
            profile.save()
        return user
    # Form Design
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
class UserProfileUpdateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    image = forms.ImageField()
    last_donation_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    street = forms.CharField(max_length=100)
    city = forms.CharField()
    post_code = forms.CharField()
    country = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # For Image Field 
        self.fields['image'].widget.attrs.update({
            'class': 'bg-gray-200',
            'required': False
        })
        # For other all fields
        for field in self.fields:
            if field != 'image':
                self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ),
                'required': False
            })
                
        if self.instance:
            try:
                user = self.instance.profile
            except UserProfile.DoesNotExist:
                    user = None

            if user:
                self.fields['gender'].initial = user.gender
                self.fields['image'].initial = user.image
                self.fields['last_donation_date'].initial = user.last_donation_date
                self.fields['street'].initial = user.street
                self.fields['city'].initial = user.city
                self.fields['post_code'].initial = user.post_code
                self.fields['country'].initial = user.country
    def clean_image(self):
            # Custom cleaning for the image field to handle optional file uploads
            image = self.cleaned_data.get('image')
            if not image and self.instance.pk:
                # If no new image is provided and the instance already has an image, keep the existing image
                return self.instance.image
            return image
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_profile, created = UserProfile.objects.get_or_create(user = user)

            user_profile.gender = self.cleaned_data['gender']
            user_profile.image = self.cleaned_data['image']
            user_profile.last_donation_date = self.cleaned_data['last_donation_date']
            user_profile.street = self.cleaned_data['street']
            user_profile.city = self.cleaned_data['city']
            user_profile.post_code = self.cleaned_data['post_code']
            user_profile.country = self.cleaned_data['country']
            
            user_profile.save()
        return user