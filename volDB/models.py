from django.db import models

# ManyToMany Relation
# A category can exist without being assigned to an organization, it can be assigned to multiple organizations
class Category(models.Model):
    category = models.CharField(db_column='category', max_length=50)
    categoryID = models.AutoField(db_column = 'categoryID', primary_key = True)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "Categories"

# ManyToMany Relation
# A location can exist without being assigned to an organization, it can be assigned to multiple organizations
class Location(models.Model):
    location = models.CharField(db_column='location', max_length=20)
    locationID = models.AutoField(db_column = 'locationID', primary_key = True)

    def __str__(self):
        return self.location
    class Meta:
        verbose_name_plural = "Locations"

# Main orgnaization model
# For single valued entries and reference to multivalued entries
# blank=True means that this field is optional
class Organization(models.Model):
    name = models.CharField(db_column='orgName', max_length = 100, blank=False)
    orgID = models.AutoField(db_column='orgID', primary_key=True)
    mission = models.TextField(db_column='missionStatement')
    opportunities = models.TextField(db_column='volOpportunities', blank=True)
    website = models.URLField(db_column='volURL', blank=True)
    notes = models.TextField(db_column='notes', blank=True)
    isVisible = models.BooleanField(db_column='visible', default=True)
    category = models.ManyToManyField(Category, db_column='category', blank=True)
    location = models.ManyToManyField(Location, db_column='location', blank=True)
    def __str__(self):
        return self.name

# An organization can have multiple phone numbers, email addresses, and/or addresses in the 
# database, but no entries in these models can exist without an orgnaization that points to it
class Phone(models.Model):
    phoneID = models.AutoField(db_column = 'phoneID', primary_key = True)
    phone = models.CharField(db_column = 'phone', max_length = 50)
    orgID = models.ForeignKey(Organization, on_delete=models.CASCADE, db_column = 'orgID')

class Email(models.Model):
    orgID = models.ForeignKey(Organization, on_delete=models.CASCADE, db_column="orgID")
    email = models.EmailField(db_column='email', max_length=254)
    emailID = models.AutoField(db_column = 'emailID', primary_key = True)

class Address(models.Model):
    orgID = models.ForeignKey(Organization, on_delete=models.CASCADE, db_column="orgID")
    addressID = models.AutoField(db_column = 'addressID', primary_key = True)
    street = models.CharField(db_column='street', max_length=100)
    city = models.CharField(db_column='city', max_length=50)
    state = models.CharField(db_column='state', max_length=20)
    zipCode = models.CharField(db_column='zipCode',max_length=20)
    isPhysicalAddress = models.BooleanField(db_column = 'isPhysicalAddress', default = False)
