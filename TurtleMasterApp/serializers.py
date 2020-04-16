from TurtleMasterApp.models import InfectionDataUs
from rest_framework import serializers


class InfectionDataUsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InfectionDataUs
        fields = ['province_state', 
        'country_region', 
        'last_update', 
        'latitude', 
        'longitude', 
        'confirmed', 
        'deaths', 
        'recovered', 
        'active', 
        'fips', 
        'incident_rate', 
        'people_tested', 
        'people_hospitalized', 
        'mortality_rate', 
        'uid', 
        'iso3', 
        'testing_rate', 
        'hospitalization_rate']