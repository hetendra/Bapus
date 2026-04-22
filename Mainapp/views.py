from django.shortcuts import render

def home(request):
    return render(request, 'coming_soon.html')