from django.contrib import admin

# Register your models here.
from . models import Category, Product


@admin.register(Category)
# make the slug field auto-populate from the name field (prepopulated_fields),
# slug will be the same as the name but in lowercase and with hyphens instead of spaces.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
