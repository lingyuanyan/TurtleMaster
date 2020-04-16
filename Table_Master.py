import sqlite3
import psycopg2
from django.conf import settings
import os
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TurtleMaster.settings')

#conn = sqlite3.connect('WC.db.sqlite')]
dbsettings = settings.DATABASES['default']
print(dbsettings)
conn = psycopg2.connect(host=dbsettings["HOST"], database=dbsettings["NAME"], user=dbsettings["USER"], password=dbsettings["PASSWORD"])
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS INFECTION_DATA_US (
    id SERIAL PRIMARY KEY,
    province_state  TEXT,
    country_region  TEXT,
    last_update  DATE, 
    confirmed  INTEGER,
    deaths  INTEGER,
    lat  DOUBLE PRECISION,
    long_  DOUBLE PRECISION,
    recovered  INTEGER,
    active  INTEGER,
    FIPS  INTEGER,
    incident_rate  DOUBLE PRECISION,
    people_tested  INTEGER,
    people_hospitalized  INTEGER,
    mortality_rate  DOUBLE PRECISION,
    UID BIGINT,
    ISO3 TEXT,
    testing_rate  DOUBLE PRECISION,
    hospitalization_rate  DOUBLE PRECISION,
    timestamp timestamp default current_timestamp,
    UNIQUE (province_state, last_update)
    )
''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = '04-14-2020.csv'
fh = open(fname, 'r')
for line in fh:
    if(line.startswith('Province_State')): continue
    pieces = line.rstrip().split(",")
    province_state = pieces[0]
    country_region = pieces[1]
    last_update = pieces[2] or date.today().strftime("%m/%d/%Y %H:%M:%S")
    lat = pieces[3]  or  '0.0'
    long_ = pieces[4]  or  '0.0'
    confirmed = pieces[5] or  '0'
    deaths = pieces[6] or  '0'
    recovered = pieces[7] or  '0'
    active = pieces[8] or  '0'
    FIPS = pieces[9] or  '0'
    incident_rate = pieces[10] or  '0.0'
    people_tested = pieces[11] or  '0'
    people_hospitalized = pieces[12] or  '0'
    mortality_rate = pieces[13] or  '0.0'
    UID = pieces[14]
    ISO3 = pieces[15]
    testing_rate = pieces[16] or  '0'
    hospitalization_rate = pieces[17] or  '0'

    insert_sql = '''INSERT INTO INFECTION_DATA_US (
        province_state, 
        country_region, 
        last_update, 
        lat, 
        long_, 
        confirmed, 
        deaths, 
        recovered, 
        active, 
        FIPS, 
        incident_rate, 
        people_tested, 
        people_hospitalized, 
        mortality_rate, 
        UID, 
        ISO3, 
        testing_rate, 
        hospitalization_rate
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (province_state, last_update) DO NOTHING
        '''

    insert_val = (
        province_state, 
        country_region, 
        last_update, 
        lat, 
        long_, 
        confirmed, 
        deaths, 
        recovered, 
        active, 
        FIPS, 
        incident_rate, 
        people_tested, 
        people_hospitalized, 
        mortality_rate, 
        UID, 
        ISO3, 
        testing_rate, 
        hospitalization_rate
        ) 
    print(insert_val)
    cur.execute(insert_sql, insert_val)

    conn.commit()
cur.execute('''SELECT * FROM INFECTION_DATA_US''')
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
