from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import json

# Create your views here.
from mysite.settings import SPOONACULAR
from django.http import JsonResponse

import requests

BASE_API_URL = "https://api.spoonacular.com"

# private API method
# gets ID and images for recipes
def getRecipesFromIngredients(request: HttpRequest):
    ingredientListString = request.GET.get("ingredients","")
    REQUEST_URL = f"{BASE_API_URL}/recipes/findByIngredients?apiKey={SPOONACULAR}&ingredients={ingredientListString}"
    JSON = requests.get(REQUEST_URL).json()
    return JsonResponse(JSON, safe=False)


# private API method
# gets JSON data and returns list of names
def autocompleteIngredients(request: HttpRequest):
    searchString = request.get("search","")
    REQUEST_URL = f"{BASE_API_URL}/food/ingredients/autocomplete?apiKey={SPOONACULAR}&query={searchString}"
    JSON = requests.get(REQUEST_URL).json()
    return HttpResponse(JSON)

