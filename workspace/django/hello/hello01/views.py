from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
app_name='hello01'
def test(request):
    return HttpResponse("<h1><a href='/test/'>A-tag Hello, Test</a></h1>")