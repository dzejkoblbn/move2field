from django.db import models


class District(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Address(models.Model):
    street_name = models.CharField(max_length=100)
    number = models.IntegerField()
    district = models.ForeignKey('District', on_delete=models.CASCADE)


class Facility(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)


class Sport(models.Model):
    TypeChoices = (('football', 'football'),
                   ('volleyball', 'volleyball'),
                   ('basketball', 'basketball'),
                   ('handball', 'handball'),
                   ('rugby', 'rugby'),
                   ('american football', 'american football'),
                   ('baseball', 'basebal'))
    type = models.CharField(max_length=50, choices=TypeChoices)
    facility = models.ForeignKey('Facility', on_delete=models.CASCADE)


class Reservation(models.Model):
    date = models.DateTimeField()
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)

# model
# serializer
# view
# podpiecie tego url do app>>urls
# python manage.py makemigration - wprowadza zmiany
# python manage.py migrate
# python manage.py runserver
# klucz obcy ma byc w tych co jest wiele łączy z pojedynczym
