from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    # overriding the display of db objects in admin interface
    list_display = ['name', 'species', 'breed', 'age', 'sex']
