from django.shortcuts import render
from django.http import HttpResponse

# index view: will render index.html upon request
def index(request):
    return render(request, 'index.html', {})