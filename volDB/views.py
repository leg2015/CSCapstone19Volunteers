from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from .models import Location
from .models import Organization
from .models import Address
from .forms import LandingPageForm
from .forms import ResultsPageForm as filterForm 

# index view: will render index.html upon request
def index(request):
    categories = Category.objects.order_by('category') # create QuerySet with all categories in volDB
    locations = Location.objects.all() # create QuerySet with all locations in volDB
    indexForm = LandingPageForm() # default form
    return render(request, 'index.html', {'categories': categories, 'locations': locations, 'indexForm': indexForm})

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
def queryRadius(Queryset, addresses, radius):
    # Search for organizations within radius of user defined location

    # Place pin for organizations within radius

    return (Queryset, addresses)

# results view: takes POST request to render results page with data from landing page form
def results(request):
    if 'refineSearch' in request.POST:
        indexForm = filterForm(request.POST)
    else:
        indexForm = LandingPageForm(request.POST) # assign form to POST request of data in LandingPageForm
        
    if indexForm.is_valid():
        form_data = indexForm.cleaned_data
        keys = form_data.keys()
        results = Organization.objects.filter(isVisible=True)
        if 'location' in keys: # field is only in LandingPageForm
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


        # create list with all orginzation IDs found in filtered results
        results_orgIDs = [result.orgID for result in results]

        # made a QuerySet of Address objects filtered from the orgIDs in the above list
        addresses = Address.objects.filter(orgID__in=results_orgIDs)
        if 'myLocation' in keys:
            print(form_data['myLocation'])
            if form_data['myLocation'] != None:
                radius = 50
                if form_data['radius'] != None:
                    radius = form_data['radius']
                results, addresses = queryRadius(results, addresses, radius)

        # zip together results and addresses to pass to results.html 
        resultsWithAddresses = zip(results, addresses)

        # create arguments dict that holds the form and filtered results to pass to 
        args = {
            'filterForm': filterForm,
            'results': results,
            'addresses': addresses,
            'resultsWithAddresses': resultsWithAddresses
        }

        # render request: uses organizationCards.html (which extends results.html)
        return render(request, 'organizationCards.html', args)

