from django.db import models
from core.models import BaseModel
from account.models import UserProfile, BloodGroup
# Create your models here.
class DonationRequest(BaseModel):
    created_by = models.ForeignKey(UserProfile, related_name="donation_request", on_delete=models.CASCADE)
    blood_group = models.ForeignKey(BloodGroup, related_name="donation_request", on_delete=models.CASCADE)
    location = models.TextField()
    description = models.TextField()
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.blood_group} by {self.created_by}"
    

class DonationReport(BaseModel):
    profile = models.ForeignKey(UserProfile, related_name="report", on_delete=models.CASCADE)
    event = models.ForeignKey(DonationRequest, related_name="report", on_delete=models.CASCADE)
