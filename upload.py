from volDB.models import *
import csv

with open('update.csv') as csvfile:
    fileReader = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in fileReader:
        if count != 0:
            org = Organization.objects.update_or_create(name=row[0], mission=row[1], opportunities=row[4], website=row[8], notes=row[9])
            org.save()
            organizationId = org.orgID
            
            # row[2] = categories
            categories = row[2].slpit('/')
            for cat in categories:
                catObj = Category.objects.get_or_create(category=cat)
                catObj.save()
                org.category.add(catObj)

            # row[3] = city/location
            locations = row[3].split('/')
            for loc in locations:
                cityObj = Location.objects.get_or_create(location=loc)
                cityObj.save()
                org.category.add(cityObj)

            # row[6] = phone number
            numbers = row[6].slpit('/')
            for num in numbers:
                Phone.objects.get_or_create(phone=num, orgid=organizationId)
                
            # row[5] = address

            # row[7] = email
            emails = row[7].split()
            for eaddress in emails:
                Email.objects.get_or_create(email=eaddress, orgID=organizationId)
        count += 1