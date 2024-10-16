from django.db import models
from django.core.validators import validate_email

class User(models.Model):
    fname = models.CharField(max_length=255)
    email = models.EmailField(validators=[validate_email], unique=True)
