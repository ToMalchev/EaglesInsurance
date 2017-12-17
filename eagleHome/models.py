from django.db import models


class info(models.Model):
    header = models.CharField(max_length=60, default='')
    text = models.TextField(default='')
    
    
class contact1(models.Model):
    contact_text = models.TextField()
    contact_phone = models.CharField(max_length=30)
    contact_email = models.EmailField()
    
    