from django.db import models

class InfectionDataUs(models.Model):
    province_state = models.TextField(blank=True, null=True)
    country_region = models.TextField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    recovered = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    fips = models.IntegerField(blank=True, null=True)
    incident_rate = models.FloatField(blank=True, null=True)
    people_tested = models.IntegerField(blank=True, null=True)
    people_hospitalized = models.IntegerField(blank=True, null=True)
    mortality_rate = models.FloatField(blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    iso3 = models.TextField(blank=True, null=True)
    testing_rate = models.FloatField(blank=True, null=True)
    hospitalization_rate = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infection_data_us'
        unique_together = (('province_state', 'last_update'),)

class InfectionDataUsStatistics(models.Model):
    province_state = models.TextField(unique=True, blank=True, null=True)
    country_region = models.TextField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    recovered = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    fips = models.IntegerField(blank=True, null=True)
    incident_rate = models.FloatField(blank=True, null=True)
    people_tested = models.IntegerField(blank=True, null=True)
    people_hospitalized = models.IntegerField(blank=True, null=True)
    mortality_rate = models.FloatField(blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    iso3 = models.TextField(blank=True, null=True)
    testing_rate = models.FloatField(blank=True, null=True)
    hospitalization_rate = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infection_data_us_statistics'


class InfectionDataWorld(models.Model):
    fips = models.IntegerField(blank=True, null=True)
    admin2 = models.TextField(blank=True, null=True)
    province_state = models.TextField(blank=True, null=True)
    country_region = models.TextField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    recovered = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    combined_key = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infection_data_world'
        unique_together = (('combined_key', 'last_update'),)


class InfectionDataWorldStatistics(models.Model):
    fips = models.IntegerField(blank=True, null=True)
    admin2 = models.TextField(blank=True, null=True)
    province_state = models.TextField(unique=True, blank=True, null=True)
    country_region = models.TextField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    recovered = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    combined_key = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infection_data_world_statistics'

class TimeSeriesDataUs(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    iso2 = models.TextField(blank=True, null=True)
    iso3 = models.TextField(blank=True, null=True)
    code3 = models.IntegerField(blank=True, null=True)
    admin2 = models.TextField(blank=True, null=True)
    combined_key = models.TextField(blank=True, null=True)
    province_state = models.TextField(blank=True, null=True)
    country_region = models.TextField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_series_data_us'
        unique_together = (('combined_key', 'last_update'),)

class TimeSeriesDataUsByState(models.Model):
    province_state = models.TextField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_series_data_us'
        unique_together = (('province_state', 'last_update'),)



class TimeSeriesDataWorld(models.Model):
    province_state = models.TextField(blank=True, null=True)
    country_region = models.TextField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    recovered = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_series_data_world'
        unique_together = (('province_state', 'last_update'),)


class ViewStatisticsData(models.Model):
    country_region = models.TextField(unique=True, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    recovered = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'view_statistics_data'