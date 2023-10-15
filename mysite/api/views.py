from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
from mysite.settings import SPOONACULAR
import requests

BASE_API_URL = "https://api.spoonacular.com"

# private API method
# gets ID and images for recipes
def getRecipesFromIngredients(request: HttpRequest):
    ingredientListString = request.GET.get("ingredients","")
    REQUEST_URL = f"{BASE_API_URL}/recipes/findByIngredients?apiKey={SPOONACULAR}&ingredients={ingredientListString}"
    JSON = requests.get(REQUEST_URL).json()
    return HttpResponse(JSON)


# private API method
# gets JSON data and returns list of names
def autocompleteIngredients(request: HttpRequest):
    searchString = request.get("search","")
    REQUEST_URL = f"{BASE_API_URL}/food/ingredients/autocomplete?apiKey={SPOONACULAR}&query={searchString}"
    JSON = requests.get(REQUEST_URL).json()
    return HttpResponse(JSON)

