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
