from django.contrib import admin
from .models import Movie,Rating
# Register your models here.

admin.site.register(Movie)
# admin.site.register(Rating)

@admin.register(Rating)
class RateAdmin(admin.ModelAdmin):
    list_display = ['user','stars']
