from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Category
from .models import Location
from .models import Organization
from .models import Address
from .forms import LandingPageForm

# index view: will render index.html upon request
def index(request):
    categories = Category.objects.order_by('category')# create QuerySet with all categories in volDB
    locations = Location.objects.all()# create QuerySet with all locations in volDB
    form = LandingPageForm()# default form
    return render(request, 'index.html', {
        'categories': categories,
        'locations': locations,
        'form': form
    })

# results view: takes POST request to render results page with data from landing page form
def results(request):
    form = LandingPageForm(request.POST)# assign form to POST request of data in LandingPageForm
    if form.is_valid():
        form_data = form.cleaned_data

    # filter organizations based on location and category chosen on landing page form
    locationSelect = form_data['location']
    categorySelect = form_data['category']

    print("Location select is ", form_data['location'])
    print("Category select is ", form_data['category'])
    if locationSelect is None and categorySelect is None:
        results = Organization.objects.all()
        print("queryset is " + str(results))
    elif locationSelect is None:
        results = Organization.objects.all().filter(category = categorySelect)
    elif categorySelect is None:
        results = Organization.objects.all().filter(location = locationSelect)
    else:
        results = Organization.objects.all().filter(location = locationSelect).filter(category = categorySelect)

    # four cases: #category is any, other is filtered# category filtered, location is any# category is any, location is any# category is filtered, location is filtered - > what we have currently

    # create list with all orginzation IDs found in filtered results
    results_orgIDs = [result.orgID for result in results]

    # made a QuerySet of Address objects filtered from the orgIDs in the above list
    addresses = Address.objects.filter(orgID__in = results_orgIDs)

    # zip together results and addresses to pass to results.html
    resultsWithAddresses = zip(results, addresses)

    # serialize addresses to JSON format to be used in main.js
    json_data = serializers.serialize("json", addresses)

    # create arguments dict that holds the form and filtered results to pass to
    args = {
        'form': form,
        'results': results,
        'addresses': addresses,
        'resultsWithAddresses': resultsWithAddresses,
        'json_data': json_data
    }

    # render request: uses organizationCards.html(which extends results.html)
    return render(request, 'organizationCards.html', args)