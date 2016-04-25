from django.contrib import admin

from . import models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'zip_code')
    search_fields = ('name', 'zip_code')
    list_filter = ('state', )
