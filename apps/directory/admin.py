from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','pk',)
    list_filter = ('name',)
    ordering = ('-pk',)