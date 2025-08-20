from django.db import models

# Create your models here.

class Salesperson(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=120)
    bio = models.TextField()

    def __str__(self):
        return self.name
