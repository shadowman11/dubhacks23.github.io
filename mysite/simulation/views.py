from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def ingredients(ingredientString: str):
    pass

# Create your views here.
def simulation(request):
    template = loader.get_template("simulation.html")
    return HttpResponse(template.render())