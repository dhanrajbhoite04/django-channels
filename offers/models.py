from django.db import models

# Create your models here.


class Offer(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=300)