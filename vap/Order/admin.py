from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.admin import TabularInline

# Register your models here.
from .models import Quote, QuoteItems

class QuoteItemsInline(TabularInline):
    model = QuoteItems
    list_display = ['item', 'quantity', 'price_per_item', 'total_price']

@admin.register(Quote)
class QuoteAdmin(ModelAdmin):
    list_display = ['company', 'quote_total_price', 'status']
    search_fields = ['company','status']
    list_filter = ['status', 'company']
    inlines = [QuoteItemsInline]
