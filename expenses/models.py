from django.db import models

# Create your models here.


class Expenses(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
# this class will be used on forms and views
