from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from .models import Location
from .models import Organization
from .forms import LandingPageForm

# index view: will render index.html upon request

def index(request):
    categories = Category.objects.order_by('category') # create QuerySet with all categories in volDB
    locations = Location.objects.all() # create QuerySet with all locations in volDB
    form = LandingPageForm()
    return render(request, 'index.html', {'categories': categories, 'locations': locations, 'form': form})

def results(request):

    form = LandingPageForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        print(form_data)

    print(form_data['category'])
    print(form_data['location'])

    results = Organization.objects.all().filter(
        location=form_data['location']
    ).filter(
        category=form_data['category']
    )

    #results = Organization.objects.all() 

    args = {
        'form': form,
        'results': results
    }

    return render(request, 'results.html', args)

# def results(request):
#     categories = Category.objects.order_by('category') # create QuerySet with all categories in volDB
#     locations = Location.objects.all() # create QuerySet with all locations in volDB
#     return render(request, 'results.html', {'categories': categories, 'locations': locations})

# TODO: figure out how to properly nest index template into base.html and use this method
# def base(request):
#    categories = Category.objects.order_by('category') # create QuerySet with all categories in volDB
#    locations = Location.objects.all() # create QuerySet with all locations in volDB
#    return render(request, 'base.html', {'categories': categories, 'locations': locations})