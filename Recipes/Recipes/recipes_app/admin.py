from django.contrib import admin

from Recipes.recipes_app.models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Recipe)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
