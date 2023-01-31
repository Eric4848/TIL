from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'tags/index.html', {'name' : 'Eric'})
    #BASE_DIR : project_name/templates
    #project_name/templates/tags/index.html