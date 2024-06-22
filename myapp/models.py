from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomerUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('Normal', 'Normal'),
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]
    # Add any additional fields you want to include
    mometary = models.IntegerField(default=0, blank=True, null=True)
    type_user = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='Normal', blank=True, null=True)

    def __str__(self):
        return self.username
