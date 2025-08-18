from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    massage = models.TextField()
    created_date = models.TimeField(auto_now_add=True)
    updated_date = models.TimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name