from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Company(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField()
    inn = models.IntegerField()
    ogrn = models.IntegerField()
    adress = models.CharField(max_length=100)
    director = models.CharField(max_length=50)

class House(models.Model):
    id = models.IntegerField()


