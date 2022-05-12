

# Create your models here.
from django.db import models


# Create your models here.
class logo(models.Model):
    logo_name = models.CharField(max_length=80)
    
    item=models.FileField()


    def __str__(self):
        return self.logo_name

