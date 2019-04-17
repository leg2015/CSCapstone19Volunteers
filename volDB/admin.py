from django.contrib import admin
from .models import *

# Register your models here.

# For registering each table separately
# admin.site.register(Organization)
# admin.site.register(Phone)

# admin.site.register(Email)

# admin.site.register(Address)

class CategoryAdmin(admin.ModelAdmin):
    def get_ordering(self, request):
        return ['category']
admin.site.register(Category, CategoryAdmin)

class LocationAdmin(admin.ModelAdmin):
    def get_ordering(self, request):
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
    list_display = ('name', 'isVisible')
    list_filter = ('category', 'location')
    inlines = [PhoneAdmin, EmailAdmin, AddressAdmin]
    search_fields = ['name']
    def get_ordering(self, request):
        return ['name']

admin.site.register(Organization, OrganizationAdmin)