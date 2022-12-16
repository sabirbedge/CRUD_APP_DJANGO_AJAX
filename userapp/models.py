from django.db import models

# Create your models here.
class Demo(models.Model):
    nm=models.TextField(default='sabir')
    mob=models.IntegerField(default='8999155937')
    city=models.TextField(default='miraj')
