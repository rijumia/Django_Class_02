from django.db import models

# Create your models here.
class userModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    birth_date = models.DateField()
