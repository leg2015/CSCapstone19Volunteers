from django.contrib import admin
from .models import *

# Register your models here.

# For registering each table separately
# admin.site.register(Organization)
# admin.site.register(Phone)

# admin.site.register(Email)

# admin.site.register(Address)
# sets organization category as a base filter for admin site
class CategoryAdmin(admin.ModelAdmin):
    def get_ordering(self, request): # orders entries alphabetically
        return ['category']
admin.site.register(Category, CategoryAdmin)
# sets location  as a base filter for admin site
class LocationAdmin(admin.ModelAdmin):
    def get_ordering(self, request): # orders entries alphabetically
        return ['location']
admin.site.register(Location, LocationAdmin)

# For registering all tables on same admin page
# https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.TabularInline
class PhoneAdmin(admin.TabularInline):
    model = Phone
class EmailAdmin(admin.TabularInline):
    model = Email  
class AddressAdmin(admin.TabularInline):
    model = Address
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'isVisible') # information to be displayed on the model page
    list_filter = ('category', 'location') # add filter options
    # enables editing these models within the same page as the orgnaizaiton admin page
    inlines = [PhoneAdmin, EmailAdmin, AddressAdmin]
    search_fields = ['name'] # adds type in search bar for organizaiton name
    def get_ordering(self, request): # orders entries alphabetically
        return ['name']

admin.site.register(Organization, OrganizationAdmin)
