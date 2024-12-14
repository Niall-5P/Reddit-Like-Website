from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_blog(request):
    # return render(request, 'home.html') # Ensure 'home.html' exists in your templates directory
    return HttpResponse("Hello, Blog!")