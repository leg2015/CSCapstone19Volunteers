from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(db_colums='orgName', max_length = 100, blank=False)
    orgID = models.AutoField(db_colums='orgID', primary_key=True)
    mission = models.TextField(db_colums='missionStatement')
    opportunities = models.TextField(db_colums='volOpportunities')
    website = models.URLField(db_colums='volURL', blank=False)
    notes = models.TextField(db_colums='notes')
