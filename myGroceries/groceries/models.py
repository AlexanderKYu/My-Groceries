from django.db import models
from user.models import User

class Tags(models.Model):
    fruit = models.BooleanField(default=False)
    vegetable = models.BooleanField(default=False)
    cannedGoods = models.BooleanField(default=False)
    dairy = models.BooleanField(default=False)
    meat = models.BooleanField(default=False)
    seafood = models.BooleanField(default=False)
    deli = models.BooleanField(default=False)
    condiment = models.BooleanField(default=False)
    snack = models.BooleanField(default=False)
    bakery = models.BooleanField(default=False)
    beverage = models.BooleanField(default=False)
    carbohydrate = models.BooleanField(default=False)
    frozen = models.BooleanField(default=False)
    personal = models.BooleanField(default=False)
    health = models.BooleanField(default=False)
    clean = models.BooleanField(default=False)


class Groceries(models.Model):

    metricEnum = (
        ("kg", "Kilogram"),
        ("g", "Gram"),
        ("lb", "Pound"),
        ("oz", "Ounce"),
        ("L", "Litre"),
        ("mL", "MilliLitre"),
        ("gal", "Gallon")
    )
    item = models.CharField(default=None, max_length=255)
    memberId = models.ForeignKey(User, on_delete=models.CASCADE)
    quant = models.IntegerField(default=None)
    metric = models.CharField(default=None, max_length=10, choices=metricEnum)
    tagId = models.ForeignKey(Tags, on_delete=models.CASCADE)
