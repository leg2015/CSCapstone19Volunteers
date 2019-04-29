from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Category
from .models import Location
from .models import Organization
from .models import Address
from .forms import LandingPageForm
from .forms import ResultsPageForm as filterForm 

# index view: will render index.html upon request
def index(request):
    categories = Category.objects.order_by('category').exclude(category='.').exclude(category='') # create QuerySet with all categories in volDB
    locations = Location.objects.exclude(location='').exclude(location='.') # create QuerySet with all locations in volDB
    indexForm = LandingPageForm()# default form
    return render(request, 'index.html', {
        'categories': categories,
        'locations': locations,
        'indexForm': indexForm
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

    #print(json_data)

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
    # categories = Category.objects.order_by('category') # create QuerySet with all categories in volDB
    # locations = Location.objects.all() # create QuerySet with all locations in volDB
    # indexForm = LandingPageForm() # default form
    # return render(request, 'index.html', {'categories': categories, 'locations': locations, 'indexForm': indexForm})

# custom logout page: will render logout.html upon request
def logout(request):
    return render(request, 'registration/logout.html')

# custom login page: will render login.html upon request
def login(self, request):
    return render(request, 'registration/login.html')

def queryCategory(Queryset, cat):
    return Queryset.filter(category=cat)
def queryLocation(Queryset, loc):
    return Queryset.filter(location=loc)

# results view: takes POST request to render results page with data from landing page form
def results(request):
    if 'refineSearch' in request.POST:
        indexForm = filterForm(request.POST)
    else:
        indexForm = LandingPageForm(request.POST) # assign form to POST request of data in LandingPageForm
        
    if indexForm.is_valid():
        form_data = indexForm.cleaned_data
        keys = form_data.keys()
        results = Organization.objects.exclude(isVisible=False).exclude(mission__exact='.').exclude(mission__exact="").exclude(location__location='.').exclude(category__category=".") #.exclude(location.location='').exclude(location.location='.') #.exclude(category__exact='.').exclude(category__exact='') .exclude(category__exact='.').exclude(location__exact='.').exclude(mission__exact='.') #.exclude(category__exact="").exclude(location__exact=""). exclude(mission__exact="")
        location = None
        if 'location' in keys: # field is only in LandingPageForm
            location = form_data['location']
            if form_data['location'] != None:
                results = queryLocation(results, form_data['location'])

        # ---- Use this if we go for single option ---- #        
        if form_data['category'] != None:  # if 'any category' is selected, don't filter by category
            results = queryCategory(results, form_data['category'])

        # ---- Use this if we go for multiselect option ---- #
        # if len(form_data['category']) > 0:
        #     for cat in form_data['category']:
        #         if cat.category != "":  # if 'any category' is selected, don't filter by category
        #             results = queryCategory(results, cat)


        # Uncomment to show all organizations in database
        # results = Organization.objects.all() 
        #TODO: use results.exclude to exclude resutls that don't have a category, mission, or city
        # results.objects.exclude(category='.')
        # results.objects.exclude(location='.')
        # results.objects.exclude(mission='.')

        # create list with all orginzation IDs found in filtered results
        results_orgIDs = [result.orgID for result in results]
       


        # made a QuerySet of Address objects filtered from the orgIDs in the above list
        addresses = Address.objects.filter(orgID__in=results_orgIDs)
        # print(keys)
        if 'myLocation' in keys:
            # print(form_data['myLocation'])
            location = form_data['myLocation']

        # zip together results and addresses to pass to results.html 
        resultsWithAddresses = zip(results, addresses)


        # serialize addresses to JSON format to be used in main.js
        json_data = serializers.serialize("json", addresses)

        print(json_data)


        category = form_data['category']
        if category != None:
            category = form_data['category'].category
        if location == "":
            location = None
        # create arguments dict that holds the form and filtered results to pass to 
        args = {
            'filterForm': filterForm,
            'results': results,
            'addresses': addresses,
            'resultsWithAddresses': resultsWithAddresses,
            'category': category,
            'location': location,
            'json_data': json_data
        }

        # render request: uses organizationCards.html (which extends results.html)
        return render(request, 'organizationCards.html', args)