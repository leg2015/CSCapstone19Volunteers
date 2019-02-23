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
    phoneID = models.AutoField(db_column = 'phoneID', primary_key = true)
    phone = models.CharField(db_column = 'phone', max_length = 10) #10 digit phone number, no dashes or spaces
    orgid = models.ForeignKey(Organization, models.DO_NOTHING, db_column = 'orgID')
