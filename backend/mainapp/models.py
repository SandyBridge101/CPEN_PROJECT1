from django.db import models

# Create your models here.
class account(models.Model):
    fname = models.CharField(max_length=80)
    lname = models.CharField(max_length=80)
    mail = models.EmailField()
    id=models.IntegerField()
    password=models.CharField
    age = models.IntegerField(max_length=80)