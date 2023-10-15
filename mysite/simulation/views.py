from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader

# Create your views here.
def simulation(request: HttpRequest):
    template = loader.get_template("simulation.html")
    return HttpResponse(template.render())