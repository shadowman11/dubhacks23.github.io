from django.urls import path
from . import views

urlpatterns = [path('getrecipes', views.getRecipesFromIngredients, name = 'recipeQuery')]