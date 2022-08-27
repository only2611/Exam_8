

from django.contrib import admin

from review.models import Product, Recall


# Register your models here.




class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'category',]
    list_display_links = ['name']
    list_filter = ['category']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'picture',]


admin.site.register(Product, ProductAdmin,)

class RecallAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'product']
    list_display_links = ['author']
    list_filter = ['author', ]
    search_fields = ['author', 'product']
    fields = ['author', 'product', 'sms', 'rate', 'moderate', 'created_at', 'updated_at', ]
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Recall, RecallAdmin)



