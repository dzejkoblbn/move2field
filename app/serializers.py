from app.models import *
from rest_framework import serializers


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')


class AddressSerializer(serializers.ModelSerializer):
    district = serializers.HyperlinkedRelatedField(queryset=District.objects.all(), view_name='districts-detail')

    class Meta:
        model = Address
        fields = ('id', 'street_name', 'number', 'district')


class FacilitySerializer(serializers.ModelSerializer):
    address = serializers.HyperlinkedRelatedField(queryset=Address.objects.all(), view_name='addresses-detail')

    class Meta:
        model = Facility
        fields = ('id', 'name', 'address')


class SportSerializer(serializers.ModelSerializer):
    facility = serializers.HyperlinkedRelatedField(queryset=Facility.objects.all(), view_name='facilities-detail')

    class Meta:
        model = Sport
        fields = ('id', 'type', 'facility')


class ReservationSerializer(serializers.ModelSerializer):
    sport = serializers.HyperlinkedRelatedField(queryset=Sport.objects.all(), view_name='sports-detail')

    class Meta:
        model = Reservation
        fields = ('id', 'date', 'sport')
