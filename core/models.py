from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Service(BaseModel):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='core/media/')

    def __str__(self) -> str:
        return self.title
    
class ContactUs(models.Model):
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 12)
    problem = models.TextField()
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact Us"