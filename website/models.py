from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    massage = models.TextField()
    created_date = models.TimeField(auto_now_add=True)
    updated_date = models.TimeField(auto_now=True)
