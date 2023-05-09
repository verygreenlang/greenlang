from django.db import models

# Create your models here.
class Token(models.Model):
    access= models.TextField(max_length=400)
    refresh= models.TextField(max_length=400)