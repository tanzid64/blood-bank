from django.db import models
from account.models import UserProfile
from core.models import BaseModel
# Create your models here.
class Event(BaseModel):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(UserProfile, related_name='event', on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    date = models.DateField()
    location = models.CharField(max_length=255)