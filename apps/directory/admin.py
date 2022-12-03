from django.contrib import admin

from .models import *



@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(HistoryStatus)
class HistoryStatusAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(ServiceProperty)
class ServicePropertyAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(ServicePropertyCheckInternal)
class ServicePropertyCheckInternalAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(ServicePropertyCheckIN)
class ServicePropertyCheckINAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(ServicePropertyCheckOUT)
class ServicePropertyCheckOUTAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(ServiceTransfer)
class ServiceTransferAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(ServiceTour)
class ServiceTourAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(ServiceExtraList)
class ServiceExtraListAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(ServiceExtra)
class ServiceExtraAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )