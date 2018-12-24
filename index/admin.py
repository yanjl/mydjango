from django.contrib import admin

from .models import Author, Book, Product, Publisher, Store

# Register your models here.
admin.AdminSite.site_header = "图书订购系统管理"
admin.AdminSite.site_title = "图书订购系统管理"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "type"]


# admin.site.register(Product, ProductAdmin)
# admin.site.register(Product)  #将模型直接注册到admin后台


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_diaplay = ['id', 'name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'price', 'rating', 'publisher', 'pubdate']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
