from TurtleMasterApp.models import InfectionDataUs
from TurtleMasterApp.models import InfectionDataUsStatistics
from TurtleMasterApp.models import InfectionDataWorld
from TurtleMasterApp.models import InfectionDataWorldStatistics
from TurtleMasterApp.models import TimeSeriesDataUs
from TurtleMasterApp.models import TimeSeriesDataWorld
from TurtleMasterApp.models import ViewStatisticsData
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

class InfectionDataUsStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InfectionDataUsStatistics
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

class InfectionDataWorldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InfectionDataWorld
        fields = ['fips', 
        'admin2', 
        'province_state', 
        'country_region', 
        'last_update', 
        'confirmed', 
        'deaths', 
        'recovered', 
        'latitude', 
        'longitude', 
        'active', 
        'combined_key']

class InfectionDataWorldStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InfectionDataWorldStatistics
        fields = ['fips', 
        'admin2', 
        'province_state', 
        'country_region', 
        'last_update', 
        'confirmed', 
        'deaths', 
        'recovered', 
        'latitude', 
        'longitude', 
        'active', 
        'combined_key']

class TimeSeriesDataUsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeSeriesDataUs
        fields = [
        'uid', 
        'iso2', 
        'iso3', 
        'code3', 
        'admin2', 
        'combined_key', 
        'province_state', 
        'country_region', 
        'last_update', 
        'latitude', 
        'longitude', 
        'confirmed', 
        'deaths']

class TimeSeriesDataUsByStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeSeriesDataUs
        fields = [
        'province_state', 
        'last_update', 
        'confirmed', 
        'deaths']

class TimeSeriesDataWorldSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = TimeSeriesDataWorld
        fields = [
        'province_state', 
        'country_region', 
        'last_update', 
        'confirmed', 
        'deaths', 
        'recovered' ]


class ViewStatisticsDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ViewStatisticsData
        fields = ['country_region', 
        'last_update', 
        'confirmed', 
        'deaths', 
        'recovered']
