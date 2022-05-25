from rest_framework import serializers

from Recipes.recipes_app.models import Category, Recipe


class CategoryForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class RecipeForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title')
