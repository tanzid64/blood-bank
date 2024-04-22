from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User
from django.utils.text import slugify
from .constants import BLOOD_TYPE, RH_FACTOR, GENDER_TYPE
from datetime import datetime, timedelta
# Create your models here.
class BloodGroup(BaseModel):
    blood_type = models.CharField(max_length=2, choices=BLOOD_TYPE)
    rh_factor = models.CharField(max_length=11, choices=RH_FACTOR)
    slug = models.SlugField(unique=True, blank=True)
    def __str__(self):
        return f"{self.blood_type} {self.rh_factor}"


class UserProfile(BaseModel):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='oldBindu/profilePictures')
    gender = models.CharField(max_length=10, choices=GENDER_TYPE, null=True, blank=True)
    blood_group = models.ForeignKey(BloodGroup, related_name='profile', on_delete=models.CASCADE)
    total_donated = models.IntegerField(default=0)
    last_donation_date = models.DateField(null=True, blank=True, default=None)
    is_available = models.BooleanField(default=True)
    street = models.CharField(max_length=50, null=True,blank=True)
    city = models.CharField(max_length=50, null=True,blank=True)
    post_code = models.CharField(max_length=5, null=True,blank=True)
    country = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    # Update is_available field auto
    def save(self, *args, **kwargs):
        today = datetime.now().date()
        three_months_ago = today - timedelta(days=90)

        if self.last_donation_date is None or self.last_donation_date <= three_months_ago:
            self.is_available = True
        else:
            self.is_available = False

        super().save(*args, **kwargs)
