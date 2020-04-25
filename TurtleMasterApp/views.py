from django.shortcuts import render
from datetime import date
import random
import math
import json
from rest_framework import viewsets
from rest_framework import permissions
from TurtleMasterApp.serializers import InfectionDataUsSerializer
from TurtleMasterApp.models import InfectionDataUs
from django.http import JsonResponse

def index(request):

    queryset = InfectionDataUs.objects.all().order_by('timestamp')
    serializer = InfectionDataUsSerializer(queryset, many=True)
    context = {'json_infection': json.dumps(serializer.data)}
    return render(request, 'TurtleMasterApp/index.html', context)

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
