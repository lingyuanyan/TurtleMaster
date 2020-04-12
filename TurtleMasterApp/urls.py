from django.urls import path
from . import views
app_name = 'TurtleMasterApp'
urlpatterns = [
# Home Page
    path('', views.index, name='index'),
]
