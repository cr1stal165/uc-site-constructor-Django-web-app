from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    inn = models.IntegerField()
    ogrn = models.IntegerField()
    address = models.CharField(max_length=500)
    director = models.CharField(max_length=128)


class House(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    kadastr_number = models.IntegerField()
    building_year = models.IntegerField()
    year_of_commissioning = models.IntegerField()
    floor = models.IntegerField()
    room = models.IntegerField()
    total_floor_space = models.IntegerField()


class Site(models.Model):
    domain = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    colors = models.CharField(max_length=100, null=True, blank=True)
    bg_colors = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='template_logo', null=True, blank=True)
    banner = models.ImageField(upload_to='template_banner', null=True, blank=True)


class News(models.Model):
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    data = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='news_image')

