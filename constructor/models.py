from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Company(models.Model):
    name = models.CharField(max_length=100)
    inn = models.IntegerField()
    ogrn = models.IntegerField()
    adress = models.CharField(max_length=100)
    director = models.CharField(max_length=50)


class House(models.Model):
    kadastr_number = models.IntegerField()
    building_year = models.IntegerField()
    year_of_commissioning = models.IntegerField()
    floor = models.IntegerField()
    room = models.IntegerField()
    total_floor_space = models.IntegerField()


class News(models.Model):
    data = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=2000)




