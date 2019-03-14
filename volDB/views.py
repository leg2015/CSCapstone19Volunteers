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
    form = LandingPageForm() # default form
    return render(request, 'index.html', {'categories': categories, 'locations': locations, 'form': form})

# results view: takes POST request to render results page with data from landing page form
def results(request):
    form = LandingPageForm(request.POST) # assign form to POST request of data in LandingPageForm
    if form.is_valid():
        form_data = form.cleaned_data

    # filter organizations based on location and category chosen on landing page form
    # results = Organization.objects.all().filter(location=form_data['location']).filter(category=form_data['category'])

    # Uncomment to show all organizations in database
    results = Organization.objects.all() 

    # create arguments dict that holds the form and filtered results to pass to 
    args = {
        'form': form,
        'results': results
    }

    # render request: uses organizationCards.html (which extends results.html)
    return render(request, 'organizationCards.html', args)