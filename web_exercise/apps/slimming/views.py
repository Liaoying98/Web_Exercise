from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.


def Center(request):
    return render(request, "slimming_center.html")
