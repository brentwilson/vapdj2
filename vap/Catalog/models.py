from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/categories', blank=True, null=True)
    meta_keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'categories'
        ordering = ['name']
        verbose_name_plural = 'Categories'
        
        
    def __unicode__(self):
        return self.name
  
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    sku = models.CharField(max_length=50)
    base_price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    image = models.ImageField(upload_to='images/products')
    lot_size = models.IntegerField(default=1000)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    current_stock = models.IntegerField(blank=True, null=True)
    description = models.TextField(null=True)
    meta_keywords = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    
    class Meta:
        db_table = 'products'
        ordering = ['name']

    class smallThumbnail:
        def _get_thumbnail(self):
            if self.image:
                return u'<img src="%s" width="125" />' % self.image.url
            else:
                return '(No image)'
        _get_thumbnail.short_description = 'Thumbnail'
        _get_thumbnail.allow_tags = True

    class largeThumbnail:
        def _get_thumbnail(self):
            if self.image:
                return u'<img src="%s" width="250" />' % self.image.url
            else:
                return '(No image)'
        _get_thumbnail.short_description = 'Thumbnail'
        _get_thumbnail.allow_tags = True
        
    def __unicode__(self):
        return self.name