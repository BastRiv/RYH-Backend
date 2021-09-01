from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','pk',)
    list_filter = ('name',)
    ordering = ('-pk',)


@admin.register(KeyResponsibility)
class KeyResponsibilityAdmin(admin.ModelAdmin):
    list_display = ('name','pk',)
    list_filter = ('name',)
    ordering = ('-pk',)


@admin.register(SkillJobs)
class SkillJobsAdmin(admin.ModelAdmin):
    list_display = ('name','pk',)
    list_filter = ('name',)
    ordering = ('-pk',)

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('name','pk',)
    list_filter = ('name',)
    ordering = ('-pk',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company','pk',)
    list_filter = ('company',)
    search_fields = ('title', )
    ordering = ('-pk',)