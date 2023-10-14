from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def frontpage(request):
    template = loader.get_template("frontpage.html")
    return HttpResponse(template.render())