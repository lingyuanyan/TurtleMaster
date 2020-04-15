from django.shortcuts import render
from datetime import date
import random
import math

def index(request):
    infection_data = []
    states = (
        "Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", 
    "California", "Colorado", "Connecticut", 
    "Delaware", "Diamond Princess",
    "District of Columbia", 
    "Florida",
    "Georgia", "Grand Princess", "Guam",
    "Hawaii",
    "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", 
    "Louisiana", 
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", 
    "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands",
    "Ohio", "Oklahoma", "Oklahoma", "Oregon", 
    "Pennsylvania", "Puerto Rico", "Rhode Island",
    "South Carolina", "South Dakota", "Tennessee", "Texas",
    "Utah", "Vermont", "Virgin Islands", "Virginia", 
    "Washington", "West Virginia", "Wisconsin", "Wyoming"
    )

    for state in states:
        infection_record = {
            "Province_State" : state,
            "Country_Region" : 'us',
            "Last_Update" : date.today() ,
            "Lat" : random.randrange(-100,100) ,
            "Long_": random.randrange(-100,100) ,
            "Confirmed":random.randint(0,100),
            "Deaths":random.randint(0,100) ,
            "Recovered" : random.randint(0,100),
            "Active":random.randint(0,100),
            "FIPS":random.randint(0,100),
            "Incident_Rate":random.randint(0,100),
            "People_Tested":random.randint(0,100),
            "People_Hospitalized":random.randint(0,100),
            "Mortality_Rate":random.randint(0,100),
            "UID":random.randint(0,100),
            "ISO3":random.randint(0,100),
            "Testing_Rate":random.randrange(0,1.0),
            "Hospitalization_Rate":random.randrange(0,1.0)
        }
        infection_data.append(infection_record)
    context = {'infection_data': infection_data}
    return render(request, 'TurtleMasterApp/index.html', context)
# Create your views here.
