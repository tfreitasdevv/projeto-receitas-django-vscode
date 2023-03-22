from django.contrib import admin
from .models import Category, Recipe

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)  # forma 1 de registrar, com o anotator @admin.register
class RecipeAdmin(admin.ModelAdmin):
    ...


# forma 2 de registrar, com a função register
admin.site.register(Category, CategoryAdmin)
