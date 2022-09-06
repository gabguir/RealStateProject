from django.db import models

# Create your models here.

class Property(models.Model):
    address = models.CharField(max_length=50)
    price = models.IntegerField()
    location =models.CharField(max_length=50)
    # status = boolean(TRUE)

    def __str__(self):
        return self.address+" "+self.location

class Agent(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)


