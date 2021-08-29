from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("A coderent website! By Tallulah, Anthony and Kenny")
