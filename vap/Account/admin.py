from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import UserAccount, Company

# Register your models here.
@admin.register(UserAccount)
class UserAccountAdmin(ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'company', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'company__name']
    list_filter = ['company', 'created_at']

@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    list_display = ['company_id', 'name', 'created_at']
    search_fields = ['company_id', 'name']
