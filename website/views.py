from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
def home_view(request):
    return HttpResponse('<h1>home page</h1>')

def about_view(request):
    return HttpResponse('<h1>about us page</h1>')

def contact_view(request):
    return HttpResponse('<h1>contacs page</h1>')