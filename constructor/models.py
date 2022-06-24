from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20,null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    inn = models.IntegerField(null=True, blank=True)
    ogrn = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    director = models.CharField(max_length=128, null=True, blank=True)


class House(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    kadastr_number = models.IntegerField(null=True, blank=True)
    building_year = models.IntegerField(null=True, blank=True)
    year_of_commissioning = models.IntegerField(null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    room = models.IntegerField(null=True, blank=True)
    total_floor_space = models.IntegerField(null=True, blank=True)


class Site(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    domain = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    colors = models.CharField(max_length=100, null=True, blank=True)
    bg_colors = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='template_logo', null=True, blank=True)
    banner = models.ImageField(upload_to='template_banner', null=True, blank=True)
    list_houses = models.FileField(upload_to='template_file', null=True, blank=True)


class News(models.Model):
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    data = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='news_image')

