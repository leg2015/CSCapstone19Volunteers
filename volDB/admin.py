from django.contrib import admin
from .models import Organization, Phone, Category, Email, Location, Address

# Register your models here.

# For registering each table separately
# admin.site.register(Organization)
# admin.site.register(Phone)
# admin.site.register(Category)
# admin.site.register(Email)
# admin.site.register(Location)
# admin.site.register(Address)

# For registering all tables on same admin page
# https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.TabularInline
class PhoneAdmin(admin.TabularInline):
    model = Phone
class CategoryAdmin(admin.TabularInline):
    model = Category
class LocationAdmin(admin.TabularInline):
    model = Location 
class EmailAdmin(admin.TabularInline):
    model = Email  
class AddressAdmin(admin.TabularInline):
    model = Address
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [CategoryAdmin, LocationAdmin, PhoneAdmin, EmailAdmin, AddressAdmin]

admin.site.register(Organization, OrganizationAdmin)