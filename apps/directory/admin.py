from django.contrib import admin

from .models import *



@admin.register(Property)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Service)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Reservation)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'property'
    )
    


