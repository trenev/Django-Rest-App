from django.urls import path

from Recipes.recipes_app.views import CategoryView, RecipesListAndCreateView

urlpatterns = (
    path('', RecipesListAndCreateView.as_view(), name='list or create recipes'),
    path('categories/', CategoryView.as_view(), name='list categories'),
)
