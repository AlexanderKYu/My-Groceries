from django.db import models
from user.models import User

class Family(models.Model):
    familyHash = models.CharField(max_length=64)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)