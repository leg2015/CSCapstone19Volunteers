from django.core.management.base import BaseCommand
from volDB.models import *
from capstone19.settings import BASE_DIR
import csv
import os
class Command(BaseCommand):
    def import_from_csv(self): 
        print('----- start import method -------')
        csvfile = open('updateCopy.csv')
        print('----- opened csv -------')
        fileReader = csv.reader(csvfile)
        print('----- csv reader -------', type(fileReader))
        count = 0
        for row in fileReader:
            print('----- row loop -------', row)
            if count != 0:
                org, created = Organization.objects.update_or_create(name=row[0], mission=row[1], opportunities=row[4], website=row[8], notes=row[9])
                
                if created:
                    org.save()
                    organizationId = org.orgID
                
                    # row[2] = categories
                    categories = row[2]
                    # for cat in categories:
                    catObj = Category.objects.get_or_create(category=catagories)
                    catObj.save()
                    org.category.add(catObj)
                    org.save()

                    # row[3] = city/location
                    location = row[3]
                    # for loc in locations:
                    cityObj = Location.objects.get_or_create(location=location)
                    cityObj.save()
                    org.category.add(cityObj)
                    org.save()

                    # row[6] = phone number
                    numbers = row[6]
                    # for num in numbers:
                    Phone.objects.get_or_create(phone=numbers, orgid=organizationId)
                        
                    # row[5] = address

                    # row[7] = email
                    emails = row[7]
                    # for eaddress in emails:
                    Email.objects.get_or_create(email=emails, orgID=organizationId)
            count += 1
    def handle(self, *args, **options):
        # call the function to import data
        print('----- made it to handle -------')
        self.import_from_csv()