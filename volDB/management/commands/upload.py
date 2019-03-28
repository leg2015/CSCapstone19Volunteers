from django.core.management.base import BaseCommand
from volDB.models import *
from capstone19.settings import BASE_DIR
import csv
import os
class Command(BaseCommand):
    def import_from_csv(self):
         
        print('----- start import method -------')
        csvfile = open('Udating NPO Caroline.csv', encoding="ISO-8859-1")
        print('----- opened csv -------')
        fileReader = csv.reader(csvfile, delimiter='|')
        print('----- csv reader -------', type(fileReader))
        count = 0
        for row in fileReader:
            print('----- row loop -------', row)
            if count != 0:
                org, created = Organization.objects.update_or_create(name=row[0], mission=row[1], opportunities=row[4], website=row[8], notes=row[9])
                
                org.save()
            
                # row[2] = categories
                categories = str(row[2]).split("`")
                for cat in categories:
                    catObj, createCat = Category.objects.get_or_create(category=cat)
                    if createCat:
                        catObj.save()
                    org.category.add(catObj)
                    org.save()

                # row[3] = city/location
                location = str(row[3]).split("`")
                for loc in location:
                    cityObj, createCity = Location.objects.get_or_create(location=loc)
                    if createCity:
                        cityObj.save()
                    org.location.add(cityObj)
                    org.save()

                # row[6] = phone number
                numbers = str(row[6]).split("`")
                for num in numbers:
                    newPhone = Phone.objects.create(phone=num, orgID=org)
                    newPhone.save()
                    
                # row[5] = address
                addresses = str(row[5]).split("`")
                for address in addresses:
                    adr = address.split(",")
                    newStreet = adr[0]
                    newCity = adr[1]
                    newState = adr[2]
                    newZip = adr[3]
                    newAddress = Address.objects.create(street=newStreet, city=newCity, state=newState, zipCode=newZip, orgID=org)
                    newAddress.save()


                # row[7] = email
                emails = str(row[7]).split("`")
                for eaddress in emails:
                    newEmail = Email.objects.create(email=eaddress, orgID=org)
                    newEmail.save()
            count += 1
    def handle(self, *args, **options):
        # call the function to import data
        print('----- made it to handle -------')
        self.import_from_csv()