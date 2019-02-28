from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from .models import Location
from .models import Organization

# index view: will render index.html upon request

def index(request):
    categories = Category.objects.order_by('category') # create QuerySet with all categories in volDB
    locations = Location.objects.all() # create QuerySet with all locations in volDB
    return render(request, 'index.html', {'categories': categories, 'locations': locations})

# TODO: figure out how to properly nest index template into base.html and use this method
def base(request):
    categories = Category.objects.order_by('category') # create QuerySet with all categories in volDB
    locations = Location.objects.all() # create QuerySet with all locations in volDB
    return render(request, 'base.html', {'categories': categories, 'locations': locations})