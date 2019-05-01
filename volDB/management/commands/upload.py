from django.core.management.base import BaseCommand
from volDB.models import *
from capstone19.settings import BASE_DIR
import csv
import os
class Command(BaseCommand):
    def import_from_csv(self):
         
        print('----- start import method -------')
        
        # ------- This file is the CSV file to be uploaded --------
        csvfile = open('UpdatingNPOAaron.csv', encoding="ISO-8859-1")
        # ---------------------------------------------------------
        
        print('----- opened csv -------')
        fileReader = csv.reader(csvfile, delimiter='|')
        print('----- csv reader -------', type(fileReader))
        count = 0
        for row in fileReader:
            print('----- row loop -------', row)
            # Ignores the first row, since it is the header row in the csv
            if count != 0:
                
                # Puts in all of the single value fields
                org, created = Organization.objects.update_or_create(name=row[0], mission=row[1], opportunities=row[4], website=row[8], notes=row[9])
                
                org.save()
            
                # row[2] = categories
                # Splits the string of categories by ` then adds an entry in the intermediate table for each.
                categories = str(row[2]).split("`")
                for cat in categories:
                    catObj, createCat = Category.objects.get_or_create(category=cat)
                    if createCat:
                        catObj.save()
                    org.category.add(catObj)
                    org.save()

                # row[3] = city/location
                # Splits the string of locations by ` then adds an entry in the intermediate table for each.
                location = str(row[3]).split("`")
                for loc in location:
                    cityObj, createCity = Location.objects.get_or_create(location=loc)
                    if createCity:
                        cityObj.save()
                    org.location.add(cityObj)
                    org.save()

                # row[6] = phone number
                # Splits the string of phone numbers by ` then adds an entry in the intermediate table for each.
                numbers = str(row[6]).split("`")
                for num in numbers:
                    newPhone = Phone.objects.create(phone=num, orgID=org)
                    newPhone.save()
                    
                # row[5] = address
                # Splits the string of addresses by '`' then splits those strings by ',' then adds an entry in 
                # the intermediate table for each address, with each substring being a piece of the address.
                addresses = str(row[5]).split("`")
                for address in addresses:
                    adr = address.split(",")
                    newStreet = adr[0]
                    newCity = adr[1]
                    newState = adr[2]
                    newZip = adr[3]
                    # This determines whether or not the address is physical or a PO box.
                    physicalAddress = True
                    if("P.O." in adr[0] or "p.o." in adr[0] or "P.o." in adr[0]):
                        physicalAddress = False
                    newAddress = Address.objects.create(street=newStreet, city=newCity, state=newState, zipCode=newZip, orgID=org, isPhysicalAddress=physicalAddress)
                    newAddress.save()
                    


                # row[7] = email
                # Splits the string of emails by ` then adds an entry in the intermediate table for each.
                emails = str(row[7]).split("`")
                for eaddress in emails:
                    newEmail = Email.objects.create(email=eaddress, orgID=org)
                    newEmail.save()
            count += 1
        print('----- finished loop -------')
    def handle(self, *args, **options):
        # call the function to import data
        print('----- made it to handle -------')
        self.import_from_csv()
