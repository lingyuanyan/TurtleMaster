"""TurtleMaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from TurtleMasterApp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'InfectionDataUs', views.InfectionDataUsViewSet)
router.register(r'InfectionDataUsStatistics', views.InfectionDataUsStatisticsViewSet)
router.register(r'InfectionDataWorld', views.InfectionDataWorldViewSet)
router.register(r'InfectionDataWorldStatistics', views.InfectionDataWorldStatisticsViewSet)
router.register(r'TimeSeriesDataUs', views.TimeSeriesDataUsViewSet)
router.register(r'TimeSeriesDataUsByState', views.TimeSeriesDataUsByStateViewSet)
router.register(r'TimeSeriesDataWorld', views.TimeSeriesDataWorldViewSet)
router.register(r'ViewStatisticsData', views.ViewStatisticsDataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include("TurtleMasterApp.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
 ]
