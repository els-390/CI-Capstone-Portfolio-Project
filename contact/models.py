from django.db import models
from about.models import ContactRequest

# Create your models here.


class ContactRequest(models.Model):
    """
    Stores a single contact request message
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact request from {self.name}"
