from django.db import models

# Create your models here.
from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     quantity = models.IntegerField()

#     def __str__(self):
#         return self.name


class students(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    def __str__(self):
        return self.name