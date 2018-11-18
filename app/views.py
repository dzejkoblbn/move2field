from rest_framework import viewsets
from app.serializers import *


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class AddressPerDistrictViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AddressSerializer

    def get_queryset(self):
        district_id = self.kwargs['district_id']
        return Address.objects.filter(district=district_id)


class FacilityPerAddressViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FacilitySerializer

    def get_queryset(self):
        address_id = self.kwargs['address_id']
        return Facility.objects.filter(address=address_id)


class SportPerFacilityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SportSerializer

    def get_queryset(self):
        facility_id = self.kwargs['facility_id']
        return Sport.objects.filter(facility=facility_id)


class ReservationPerSportViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        sport_id = self.kwargs['sport_id']
        return Reservation.objects.filter(sport_id=sport_id)
