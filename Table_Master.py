import sqlite3
import psycopg2
from django.conf import settings
import os
from datetime import date
import sys
import csv


def parser_us_data(fname):
    print("parse us data in file:", fname)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TurtleMaster.settings')
    # conn = sqlite3.connect('WC.db.sqlite')]
    dbsettings = settings.DATABASES['default']
    print(dbsettings)
    conn = psycopg2.connect(host=dbsettings["HOST"], database=dbsettings["NAME"],
                            user=dbsettings["USER"], password=dbsettings["PASSWORD"])
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS INFECTION_DATA_US (
        id SERIAL PRIMARY KEY,
        province_state  TEXT,
        country_region  TEXT,
        last_update  DATE,
        confirmed  INTEGER,
        deaths  INTEGER,
        latitude  DOUBLE PRECISION,
        longitude  DOUBLE PRECISION,
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

    fh = open(fname, 'r')
    csv_reader = csv.reader(fh)
    for line in csv_reader:
        pieces = line
        if(pieces[0] == 'Province_State'): continue
        if(pieces[0] == 'Recovered'): continue
        province_state = pieces[0]
        country_region = pieces[1]
        last_update = pieces[2] or date.today().strftime("%m/%d/%Y %H:%M:%S")
        latitude = pieces[3] or '0.0'
        longitude = pieces[4] or '0.0'
        confirmed = pieces[5] or '0'
        deaths = pieces[6] or '0'
        recovered = (pieces[7] or '0').rstrip('.')
        actp = (pieces[8] or '0').strip(".")
        active = actp[0]
        FIPS = pieces[9] or '0'
        incident_rate = pieces[10] or '0.0'
        people_tested = pieces[11] or '0'
        people_hospitalized = pieces[12] or '0'
        mortality_rate = pieces[13] or '0.0'
        UID = pieces[14]
        ISO3 = pieces[15]
        testing_rate = pieces[16] or '0'
        hospitalization_rate = pieces[17] or '0'

        insert_sql = '''INSERT INTO INFECTION_DATA_US (
            province_state,
            country_region,
            last_update,
            latitude,
            longitude,
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
            latitude,
            longitude,
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

 #   cur.execute('''SELECT * FROM INFECTION_DATA_US''')
 #   rows = cur.fetchall()
 #   print(rows.)
 #   for row in rows:
 #       print(row)
    cur.close()


def parser_world_data(fname):
    print("parse world data in file:", fname)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TurtleMaster.settings')
    # conn = sqlite3.connect('WC.db.sqlite')]
    dbsettings = settings.DATABASES['default']
    print(dbsettings)
    conn = psycopg2.connect(host=dbsettings["HOST"], database=dbsettings["NAME"],
                            user=dbsettings["USER"], password=dbsettings["PASSWORD"])
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS INFECTION_DATA_WORLD (
        id SERIAL PRIMARY KEY,
        FIPS  INTEGER,
        admin2 TEXT,
        province_state  TEXT,
        country_region  TEXT,
        last_update  DATE,
        confirmed  INTEGER,
        deaths  INTEGER,
        latitude  DOUBLE PRECISION,
        longitude  DOUBLE PRECISION,
        recovered  INTEGER,
        active  INTEGER,
        combined_Key TEXT,
        timestamp timestamp default current_timestamp,
        UNIQUE (province_state, last_update)
        )
    ''')

    fh = open(fname, 'r')
    csv_reader = csv.reader(fh)
    key_pos_dic = {}
    for line in csv_reader:
        pieces = line
        if(pieces[0].endswith('FIPS') or pieces[0].endswith('Province/State')):
            index=0
            for piece in pieces:
                key=piece.lower()
                if key.endswith('province/state'): key="province_state"
                if key.endswith('province_state'): key="province_state"
                if key.endswith('fips'): key="fips"
                if key == 'country/region': key="country_region"
                if key == 'lat': key="latitude"
                if key == 'long_': key="longitude"
                if key == 'combined key': key="combined_key"
                if key == 'last update': key="last_update"
                key_pos_dic[key]=index
                index += 1
            continue
        if(pieces[0] == 'Recovered'): continue

        province_state=pieces[key_pos_dic["province_state"]]
        country_region=pieces[key_pos_dic["country_region"]]
        last_update=pieces[key_pos_dic["last_update"]] or date.today().strftime("%m/%d/%Y %H:%M:%S")
        latitude=pieces[key_pos_dic["latitude"]] or '0.0' if "latitude" in key_pos_dic else '0.0'
        longitude=pieces[key_pos_dic["longitude"]] or '0.0' if "longitude" in key_pos_dic else '0.0'
        confirmed=pieces[key_pos_dic["confirmed"]] or '0' if "fips" in key_pos_dic else '0'
        deaths=pieces[key_pos_dic["deaths"]] or '0' if "fips" in key_pos_dic else '0'
        recovered=(pieces[key_pos_dic["recovered"]] or '0').split('.')[0] if "recovered" in key_pos_dic else '0'
        active=(pieces[key_pos_dic["active"]] or '0').split(".")[0] if "active" in key_pos_dic else '0'
        FIPS=pieces[key_pos_dic["fips"]] or '0' if "fips" in key_pos_dic else '0'
        admin2=pieces[key_pos_dic["admin2"]] if "admin2" in key_pos_dic else ""
        combined_key=pieces[key_pos_dic["combined_key"]] if "combined_key" in key_pos_dic else ""

        insert_sql='''INSERT INTO INFECTION_DATA_WORLD (
            FIPS,
            admin2,
            province_state,
            country_region,
            last_update,
            confirmed,
            deaths,
            latitude,
            longitude,
            recovered,
            active,
            combined_key
           )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (province_state, last_update) DO NOTHING
            '''

        insert_val=(
            FIPS,
            admin2,
            province_state,
            country_region,
            last_update,
            confirmed,
            deaths,
            latitude,
            longitude,
            recovered,
            active,
            combined_key,
           )
        print(insert_val)
        cur.execute(insert_sql, insert_val)

        conn.commit()

 #   cur.execute('''SELECT * FROM INFECTION_DATA_US''')
 #   rows = cur.fetchall()
 #   print(rows.)
 #   for row in rows:
 #       print(row)
    cur.close()
def iterate_files(folder_path, data_type):
    print("Iterate in  ", folder_path)
    for filename in os.listdir(folder_path):
        fullpath=os.path.join(folder_path, filename)
        if not filename.startswith("_") and not filename.startswith(".") and filename.endswith(".csv"):
            try:
                if(data_type == "us"):
                    parser_us_data(fullpath)
                if(data_type == "world"):
                    parser_world_data(fullpath)
            except:
                print(sys.exc_info()[0])
                quit()

default_folder=os.path.abspath(os.path.join(
    os.getcwd(), "../COVID-19/csse_covid_19_data/"))
us_data_folder="csse_covid_19_daily_reports_us"
world_data_folder="csse_covid_19_daily_reports"

root_directory=input("Enter folder name: ")
if (len(root_directory) < 1): root_directory=default_folder
us_data_full_path=os.path.join(root_directory, us_data_folder)
world_data_full_path=os.path.join(root_directory, world_data_folder)
iterate_files(us_data_full_path, "us")
iterate_files(world_data_full_path, "world")
