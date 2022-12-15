from django.db import models

# Create your models here.
class User(models.Model):
    nm=models.CharField(max_length=20)
    mob=models.IntegerField()
    city=models.CharField(max_length=20)
