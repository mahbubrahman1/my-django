from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def test(request):
#     return HttpResponse("hello! world")

def test(request):
    return HttpResponse("<h1>hello! world</h2>")
