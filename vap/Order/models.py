from django.db import models
from Catalog.models import Product
from Account.models import Company

class Quote(models.Model):

    class STATUSCHOICES(models.TextChoices):
        QUOTE = 'Quote'
        READY = 'Ready For Review'
        WORKORDER = 'Work Order'
        INVOICE= 'Invoice'
        CANCELED = 'Canceled'
        PAID = 'Paid'


    quoteId = models.CharField(max_length=255, primary_key=True)
    document_date = models.DateField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUSCHOICES.choices, default=STATUSCHOICES.QUOTE)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def quote_total_price(self):
        total = 0
        for item in self.quoteitems_set.all():
            total += item.total_price()
        return total
    
    def __str__(self):
        return self.name

class QuoteItems(models.Model):
    quoteId = models.ForeignKey(Quote, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    list_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['list_order']
        verbose_name_plural = 'Quote Items'
    
    def __str__(self):
        return self.name
    
    def total_price(self):
        return self.quantity * self.price_per_item
