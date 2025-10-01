from django.contrib import admin
from .models import Bakery

# Register your models here.
# admin.site.register(Bakery)

@admin.register(Bakery)
class Bakeryadmin(admin.ModelAdmin):
    list_display = ('name', 'rating')