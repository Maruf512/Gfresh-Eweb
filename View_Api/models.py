from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    passwd = models.CharField(max_length=50)

    def __str__(self):
        return self.email