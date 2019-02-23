from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(db_column='orgName', max_length = 100, blank=False)
    orgID = models.AutoField(db_column='orgID', primary_key=True)
    mission = models.TextField(db_column='missionStatement')
    opportunities = models.TextField(db_column='volOpportunities')
    website = models.URLField(db_column='volURL', blank=False)
    notes = models.TextField(db_column='notes')


class Phone(models.Model):
    phoneID = models.AutoField(db_column = 'phoneID', primary_key = True)
    phone = models.CharField(db_column = 'phone', max_length = 10) #10 digit phone number, no dashes or spaces
    orgid = models.ForeignKey(Organization, models.DO_NOTHING, db_column = 'orgID')

class Category(models.Model):
    orgID = models.ForeignKey(Organization, models.DO_NOTHING, db_column="orgID")
    category = models.CharField(db_column='category', max_length=20)
    categoryID = models.AutoField(db_column = 'categoryID', primary_key = True)

class Email(models.Model):
    orgID = models.ForeignKey(Organization, models.DO_NOTHING, db_column="orgID")
    email = models.EmailField(db_column='email', max_length=254)
    emailID = models.AutoField(db_column = 'emailID', primary_key = True)

class Location(models.Model):
    orgID = models.ForeignKey(Organization, models.DO_NOTHING, db_column="orgID")
    location = models.CharField(db_column='location', max_length=20)
    locationID = models.AutoField(db_column = 'locationID', primary_key = True)

class Address(models.Model):
    orgID = models.ForeignKey(Organization, models.DO_NOTHING, db_column="orgID")
    addressID = models.AutoField(db_column = 'addressID', primary_key = True)
    street = models.CharField(db_column='street', max_length=100)
    city = models.CharField(db_column='city', max_length=20)
    state = models.CharField(db_column='state')
    zipCode = models.IntegerField(db_column='zipCode', max_length=50)