from django.conf.urls import include, url
from rest_framework import routers
from app.views import *

router = routers.DefaultRouter()
router.register(r'districts', DistrictViewSet, base_name='districts')
router.register(r'addresses', AddressViewSet, base_name='addresses')
router.register(r'facilities', FacilityViewSet, base_name='facilities')
router.register(r'sports', SportViewSet, base_name='sports')
router.register(r'reservations', ReservationViewSet, base_name='reservations')
router.register(r'districts/(?P<district_id>\d+)/addresses', AddressPerDistrictViewSet,
                base_name='addresses_per_district')
router.register(r'addresses/(?P<address_id>\d+)/facilities', FacilityPerAddressViewSet,
                base_name='facilities_per_address')
router.register(r'facilities/(?P<facility_id>\d+)/sports', SportPerFacilityViewSet,
                base_name='sports_per_facility')
router.register(r'sports/(?P<sport_id>\d+)/reservations', ReservationPerSportViewSet,
                base_name='reservation_per_sport')

urlpatterns = [
    url(r'^', include(router.urls))
]
