from django.db import models


# Create your models here

class Address(models.Model):
    streetAddress = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipCode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.streetAddress + " " + self.city + " " + self.state + " " + self.zipCode + " " + self.country


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    car_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name + " " + " " + self.email + " " + self.phone


class Account(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name + " " + self.password + " " + self.person + " " + self.status




