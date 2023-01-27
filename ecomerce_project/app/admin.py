from django.contrib import admin

from .models import (
Customer,
Product,
Recommendation,
)
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
     list_display = ['id','title','selling_price','discounted_price','description','brand','category','product_image']

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display=['id','Product_id','Customer_id']