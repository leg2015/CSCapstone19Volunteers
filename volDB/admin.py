from django.contrib import admin
from .models import Organization, Phone, Category, Email, Location, Address

# Register your models here.
admin.site.register(Organization)
admin.site.register(Phone)
admin.site.register(Category)
admin.site.register(Email)
admin.site.register(Location)
admin.site.register(Address)