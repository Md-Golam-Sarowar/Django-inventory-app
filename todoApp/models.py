from django.db import models

# Create your models here.
class item(models.Model):
    content = models.TextField(default="")
    name = models.TextField(default="")
    price = models.IntegerField(default=0)
