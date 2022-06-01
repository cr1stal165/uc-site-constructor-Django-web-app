from django.contrib import admin
from .models import User, Company


@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    pass


