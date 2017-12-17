from django.db import models

# Create your models here.
class Insurance1(models.Model):
    titleInsurance = models.CharField(max_length=100)
    descriptionInsurance = models.TextField()
    insurance_type = models.CharField(max_length=50)
    date = models.DateTimeField()
    image = models.ImageField(default=None)
    def __str__(self):
        return self.titleInsurance