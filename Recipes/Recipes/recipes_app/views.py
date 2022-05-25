from rest_framework import generics as api_views, permissions

from Recipes.recipes_app.models import Category, Recipe
from Recipes.recipes_app.serializers import CategoryForListSerializer, RecipeForListSerializer


class CategoryView(api_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryForListSerializer
    permission_classes = (
        permissions.AllowAny,
    )


class RecipesListAndCreateView(api_views.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeForListSerializer
    permission_classes = (
        permissions.AllowAny,
    )
