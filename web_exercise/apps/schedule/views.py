from django.shortcuts import render

# Create your views here.


def Center(request):
    return render(request, "schedule_center.html")