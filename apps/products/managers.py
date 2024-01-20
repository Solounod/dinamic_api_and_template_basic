from django.db import models

class ProductManager(models.Manager):
    
    def get_search_products(self, keyword):
        return self.filter(
            models.Q(name__icontains=keyword) |
            models.Q(price__icontains=keyword) |
            models.Q(category__categoryproduct__icontains=keyword)
        ).order_by('-id')