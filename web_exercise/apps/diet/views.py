from django.shortcuts import render

# Create your views here.


def Center(request):
    return render(request, "diet_center.html")


def single(request):
    return render(request, "single.html")