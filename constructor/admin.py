from django.contrib import admin
from .models import User, Company, House


@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass

