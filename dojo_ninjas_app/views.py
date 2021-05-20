from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    return render(request, "index.html")
