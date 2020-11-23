from django.shortcuts import render
from datetime import date
import random
import math
import json
from rest_framework import viewsets
from rest_framework import permissions
from TurtleMasterApp.serializers import InfectionDataUsSerializer
from TurtleMasterApp.serializers import InfectionDataUsStatisticsSerializer
from TurtleMasterApp.serializers import InfectionDataWorldSerializer
from TurtleMasterApp.serializers import InfectionDataWorldStatisticsSerializer
from TurtleMasterApp.serializers import TimeSeriesDataUsSerializer, TimeSeriesDataUsByStateSerializer
from TurtleMasterApp.serializers import TimeSeriesDataWorldSerializer
from TurtleMasterApp.serializers import ViewStatisticsDataSerializer
from TurtleMasterApp.models import InfectionDataUs
from TurtleMasterApp.models import InfectionDataUsStatistics
from TurtleMasterApp.models import InfectionDataWorld
from TurtleMasterApp.models import InfectionDataWorldStatistics
from TurtleMasterApp.models import TimeSeriesDataUs,TimeSeriesDataUsByState
from TurtleMasterApp.models import TimeSeriesDataWorld
from TurtleMasterApp.models import ViewStatisticsData
from django.http import JsonResponse
from django.db.models import Sum

def index(request):

    queryset_topline = ViewStatisticsData.objects.all().order_by('timestamp')
    serializer_topeline = ViewStatisticsDataSerializer(queryset_topline, many=True)

    queryset_us_statistics = InfectionDataUsStatistics.objects.all().order_by('timestamp')
    serializer_us_statistics = InfectionDataUsStatisticsSerializer(queryset_us_statistics, many=True)

    queryset_world_statistics = InfectionDataWorldStatistics.objects.all().order_by('timestamp')
    serializer_world_statistics = InfectionDataWorldStatisticsSerializer(queryset_world_statistics, many=True)

    queryset_time_series_us = TimeSeriesDataUs.objects.all().order_by('timestamp')
    serializer_time_series_us = TimeSeriesDataUsSerializer(queryset_time_series_us, many=True)

    context = {
        'json_topline': json.dumps(serializer_topeline.data),
        'json_us_statistics': json.dumps(serializer_us_statistics.data),
        'json_world_statistics': json.dumps(serializer_world_statistics.data),
        'json_time_series_us':json.dumps(serializer_time_series_us.data),
    }


    return render(request, 'index.html', context)

class InfectionDataUsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InfectionDataUs.objects.all().order_by('timestamp')
    serializer_class = InfectionDataUsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `province_state` query parameter in the URL.
        """
        queryset = InfectionDataUs.objects.all().order_by('timestamp')

        province_state = self.request.query_params.get('province_state', None)
        if province_state is not None:
            queryset = queryset.filter(province_state=province_state)
        return queryset
# Create your views here.

class InfectionDataUsStatisticsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InfectionDataUsStatistics.objects.all().order_by('timestamp')
    serializer_class = InfectionDataUsStatisticsSerializer
    permission_classes = [permissions.AllowAny]

class InfectionDataWorldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InfectionDataWorld.objects.all().order_by('timestamp')
    serializer_class = InfectionDataWorldSerializer
    permission_classes = [permissions.AllowAny]

class InfectionDataWorldStatisticsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InfectionDataWorldStatistics.objects.all().order_by('timestamp').exclude(country_region = 'US')
    serializer_class = InfectionDataWorldStatisticsSerializer
    permission_classes = [permissions.AllowAny]

class TimeSeriesDataUsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TimeSeriesDataUs.objects.all().order_by('timestamp')
    serializer_class = TimeSeriesDataUsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `province_state` query parameter in the URL.
        """
        distinct_on = self.request.query_params.get('distinct_on', None)
        province_state = self.request.query_params.get('province_state', None)
        if distinct_on is not None:
            queryset = TimeSeriesDataUs.objects.all().order_by(distinct_on).distinct(distinct_on)
        else:
            queryset = TimeSeriesDataUs.objects.all().order_by('timestamp')

        if province_state is not None:
            queryset = queryset.filter(province_state = province_state)

        return queryset

class TimeSeriesDataUsByStateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TimeSeriesDataUsByState.objects.all().order_by('last_update')
    serializer_class = TimeSeriesDataUsByStateSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `province_state` query parameter in the URL.
        """
        distinct_on = self.request.query_params.get('distinct_on', None)
        province_state = self.request.query_params.get('province_state', None)
        if distinct_on is not None:
            queryset = TimeSeriesDataUsByState.objects\
                .all().order_by(distinct_on).distinct(distinct_on)
        else:
            queryset = TimeSeriesDataUsByState.objects\
                .values('province_state','last_update')\
                    .annotate(confirmed = Sum('confirmed'), deaths = Sum('deaths'))

        if province_state is not None:
            queryset = queryset.filter(province_state = province_state)

        return queryset
class TimeSeriesDataWorldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TimeSeriesDataWorld.objects.all().order_by('timestamp')
    serializer_class = TimeSeriesDataWorldSerializer
    permission_classes = [permissions.AllowAny]

class ViewStatisticsDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ViewStatisticsData.objects.all().order_by('timestamp')
    serializer_class = ViewStatisticsDataSerializer
    permission_classes = [permissions.AllowAny]
