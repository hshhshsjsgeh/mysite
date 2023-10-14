"""
views
"""
# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    index page
    """
    return HttpResponse('Hello, world. You\'re at the polls index.' + request.method)
