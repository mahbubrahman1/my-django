from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hi there, I'm in the homepage</h1>")
