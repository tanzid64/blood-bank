from django.db import models
from django.utils.text import slugify
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Service(BaseModel):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=350, unique=True, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='core/media/')

    def __str__(self) -> str:
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
class ContactUs(BaseModel):
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 12)
    problem = models.TextField()
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact Us"

