from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=255)
    email = models.EmailField()
