# Generated by Django 3.1 on 2020-09-06 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TurtleMasterApp', '0002_auto_20200525_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSeriesDataUsByState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_state', models.TextField(blank=True, null=True)),
                ('last_update', models.DateField(blank=True, null=True)),
                ('confirmed', models.IntegerField(blank=True, null=True)),
                ('deaths', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'time_series_data_us',
                'managed': False,
            },
        ),
    ]
