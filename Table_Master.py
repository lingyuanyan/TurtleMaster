import sqlite3
import psycopg2
from django.conf import settings
import os
from datetime import date
import time
import sys
import csv
import re
import traceback

def parser_us_data(fname, drop_table):
    print("parse us data in file:", fname)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TurtleMaster.settings')
    # conn = sqlite3.connect('WC.db.sqlite')]
    dbsettings = settings.DATABASES['default']

    conn = psycopg2.connect(host=dbsettings["HOST"], database=dbsettings["NAME"],
                            user=dbsettings["USER"], password=dbsettings["PASSWORD"])
    cur = conn.cursor()
    if(drop_table == 'yes') :
        cur.execute('''
        DROP TABLE IF EXISTS INFECTION_DATA_US
        ''')
        cur.execute('''
        DROP TABLE IF EXISTS INFECTION_DATA_US_STATISTICS
        ''')

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

    cur.execute('''
    CREATE TABLE IF NOT EXISTS INFECTION_DATA_US_STATISTICS (
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
        UNIQUE (province_state)
        )
    ''')
    num_line = 0
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
        recovered = str(int(float((pieces[7] or '0'))))
        active = str(int(float((pieces[8] or '0'))))
        FIPS = str(int(float((pieces[9] or '0'))))
        incident_rate = pieces[10] or '0.0'
        people_tested = str(int(float((pieces[11] or '0'))))
        people_hospitalized = str(int(float((pieces[12] or '0'))))
        mortality_rate = pieces[13] or '0.0'
        UID = str(int(float((pieces[14] or '0'))))
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

        insert_sql_stat = '''INSERT INTO INFECTION_DATA_US_STATISTICS (
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
            ON CONFLICT (province_state) DO NOTHING
            '''
        update_sql_stat = '''
            UPDATE INFECTION_DATA_US_STATISTICS
            SET
                country_region = %s,
                last_update = %s,
                latitude = %s,
                longitude = %s,
                confirmed = %s,
                deaths = %s,
                recovered = %s,
                active = %s,
                FIPS = %s,
                incident_rate = %s,
                people_tested = %s,
                people_hospitalized = %s,
                mortality_rate = %s,
                UID = %s,
                ISO3 = %s,
                testing_rate= %s,
                hospitalization_rate = %s
            WHERE province_state = %s and last_update < %s::date + '1 day'::interval
            RETURNING last_update
            '''

        update_val_stat = (
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
            hospitalization_rate,
            province_state,
            last_update
            )

        cur.execute(insert_sql, insert_val)
        cur.execute(insert_sql_stat, insert_val)

        if cur.rowcount == 0 :
            cur.execute(update_sql_stat, update_val_stat)

        conn.commit()
        num_line+=1
        print(num_line, " of lines has been processed", num_line, end='\r', flush=True)

 #   cur.execute('''SELECT * FROM INFECTION_DATA_US''')
 #   rows = cur.fetchall()
 #   print(rows.)
 #   for row in rows:
 #       print(row)
    cur.close()
    print(num_line, " of lines has been processed")

def parser_world_data(fname, drop_table):
    print("parse world data in file:", fname)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TurtleMaster.settings')
    # conn = sqlite3.connect('WC.db.sqlite')]
    dbsettings = settings.DATABASES['default']

    conn = psycopg2.connect(host=dbsettings["HOST"], database=dbsettings["NAME"],
                            user=dbsettings["USER"], password=dbsettings["PASSWORD"])
    cur = conn.cursor()

    if(drop_table == 'yes') :
        cur.execute('''
        DROP TABLE IF EXISTS INFECTION_DATA_WORLD
        ''')
        cur.execute('''
        DROP TABLE IF EXISTS INFECTION_DATA_WORLD_STATISTICS
        ''')

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
        UNIQUE (combined_Key, last_update)
        )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS INFECTION_DATA_WORLD_STATISTICS (
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
        UNIQUE (combined_Key)
        )
    ''')
    num_line = 0
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

        country_region = pieces[key_pos_dic["country_region"]]
        province_state = pieces[key_pos_dic["province_state"]] or country_region
        last_update = pieces[key_pos_dic["last_update"]] or date.today().strftime("%m/%d/%Y %H:%M:%S")
        latitude = pieces[key_pos_dic["latitude"]] or '0.0' if "latitude" in key_pos_dic else '0.0'
        longitude = pieces[key_pos_dic["longitude"]] or '0.0' if "longitude" in key_pos_dic else '0.0'
        confirmed = pieces[key_pos_dic["confirmed"]] or '0' if "confirmed" in key_pos_dic else '0'
        deaths = pieces[key_pos_dic["deaths"]] or '0' if "deaths" in key_pos_dic else '0'
        recovered = (pieces[key_pos_dic["recovered"]] or '0').split('.')[0] if "recovered" in key_pos_dic else '0'
        active = (pieces[key_pos_dic["active"]] or '0').split(".")[0] if "active" in key_pos_dic else '0'
        FIPS = str(int(float(pieces[key_pos_dic["fips"]] or '0' if "fips" in key_pos_dic else '0')))
        admin2 = pieces[key_pos_dic["admin2"]] if "admin2" in key_pos_dic else ""
        combined_key = pieces[key_pos_dic["combined_key"]] if "combined_key" in key_pos_dic else ""

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
            ON CONFLICT (combined_Key, last_update) DO NOTHING
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
        cur.execute(insert_sql, insert_val)

        insert_sql_stat='''INSERT INTO INFECTION_DATA_WORLD_STATISTICS (
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
            ON CONFLICT (combined_Key) DO NOTHING
            '''

        update_sql_stat='''UPDATE INFECTION_DATA_WORLD_STATISTICS SET (
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
            active
           )
            = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            WHERE combined_Key = %s and last_update < %s::date + '1 day'::interval
            RETURNING last_update
            '''
        update_val=(
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
            last_update
           )

        cur.execute(insert_sql_stat, insert_val)

        if cur.rowcount == 0 :
           cur.execute(update_sql_stat, update_val)
        conn.commit()
        num_line += 1
        print(num_line, " of lines has been processed", num_line, end='\r', flush=True)

 #   cur.execute('''SELECT * FROM INFECTION_DATA_US''')
 #   rows = cur.fetchall()
 #   print(rows.)
 #   for row in rows:
 #       print(row)
    cur.close()
    print(num_line, " of lines has been processed")


def parser_time_series_data_us(fname, drop_table):
    print("parser_time_series_data_us: ", fname)
    file_suffix = "_US.csv"
    if not fname.endswith(file_suffix) :
        print("not ", file_suffix, " ... skipped")
        return
    update_key = "confirmed" if fname.lower().find("confirmed") >= 0 else "deaths" if fname.lower().find("deaths") >= 0 else None
    if not update_key :
        print("not finding update key (confirmed | deaths | recovered) in file name...skipped")
        return

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TurtleMaster.settings')
    # conn = sqlite3.connect('WC.db.sqlite')]
    dbsettings = settings.DATABASES['default']

    conn = psycopg2.connect(host=dbsettings["HOST"], database=dbsettings["NAME"],
                            user=dbsettings["USER"], password=dbsettings["PASSWORD"])
    cur = conn.cursor()

    if(drop_table == 'yes' and update_key == 'confirmed') :
        cur.execute('''
        DROP TABLE IF EXISTS TIME_SERIES_DATA_US
        ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS TIME_SERIES_DATA_US (
        id SERIAL PRIMARY KEY,
        uid  INTEGER,
        iso2 TEXT,
        iso3 TEXT,
        code3 INTEGER,
        admin2 TEXT,
        combined_key TEXT,
        province_state  TEXT,
        country_region  TEXT,
        last_update  DATE,
        latitude  DOUBLE PRECISION,
        longitude  DOUBLE PRECISION,
        confirmed  INTEGER,
        deaths  INTEGER,
        timestamp timestamp default current_timestamp,
        UNIQUE (combined_key, last_update)
        )
    ''')
    num_line = 0
    fh = open(fname, 'r')
    csv_reader = csv.reader(fh)
    key_pos_dic = {}
    date_key_dic = {}
    for line in csv_reader:
        pieces = line
        if(pieces[0].endswith('UID') or pieces[0].endswith('Province/State')):
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
                date_key = re.search(r'(\d+(/|-){1}\d+(/|-){1}\d{2,4})',key)
                if date_key is not None :  date_key_dic[key] = index
                index += 1
            continue
        if(pieces[0] == 'Recovered'): continue

        country_region=pieces[key_pos_dic["country_region"]]
        province_state=pieces[key_pos_dic["province_state"]] or country_region
        latitude=pieces[key_pos_dic["latitude"]] or '0.0' if "latitude" in key_pos_dic else '0.0'
        longitude=pieces[key_pos_dic["longitude"]] or '0.0' if "longitude" in key_pos_dic else '0.0'
        admin2=pieces[key_pos_dic["admin2"]] if "admin2" in key_pos_dic else ""
        combined_key=pieces[key_pos_dic["combined_key"]] if "combined_key" in key_pos_dic else ""
        uid  = (pieces[key_pos_dic["uid"]] or '0').split('.')[0] if "uid" in key_pos_dic else '0'
        iso2 =pieces[key_pos_dic["iso2"]] or '0' if "iso2" in key_pos_dic else ''
        iso3 =pieces[key_pos_dic["iso3"]] or '0' if "iso3" in key_pos_dic else ''
        code3 =(pieces[key_pos_dic["code3"]] or '0').split('.')[0] if "code3" in key_pos_dic else '0'
        for date_key in date_key_dic :
            last_update = date_key
            updte_value = pieces[date_key_dic[date_key]]
            insert_sql='''INSERT INTO TIME_SERIES_DATA_US (
                uid,
                iso2,
                iso3,
                code3,
                admin2,
                province_state,
                country_region,
                latitude,
                longitude,
                combined_key,
                last_update,
                confirmed,
                deaths
            )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (combined_key, last_update) DO NOTHING
                '''

            insert_val=(
                uid,
                iso2,
                iso3,
                code3,
                admin2,
                province_state,
                country_region,
                latitude,
                longitude,
                combined_key,
                last_update,
                '0',
                '0'
            )
            cur.execute(insert_sql, insert_val)

            update_sql_stat='''UPDATE TIME_SERIES_DATA_US SET
                {} = %s
                WHERE combined_key = %s and last_update = %s::date
                RETURNING last_update
                '''.format(update_key)
            update_val=(
                updte_value,
                combined_key,
                last_update
            )
            cur.execute(update_sql_stat, update_val)

            num_line += 1
            print(num_line, " of lines has been processed", num_line, end='\r', flush=True)
    conn.commit()
    cur.close()
    print(num_line, " of lines has been processed", num_line)


def parser_time_series_data_global(fname, drop_table):
    print("parser_time_series_data_global: ", fname)
    file_suffix = "_global.csv"
    if not fname.endswith(file_suffix) :
        print("not a ", file_suffix, " ...skipped")
        return

    update_key = "confirmed" if fname.lower().find("confirmed") \
    else "deaths" if fname.lower().find("deaths") \
    else "recovered" if fname.lower().find("recovered") \
    else None

    if not update_key :
        print("not finding update key (confirmed | deaths | recovered) in file name...skipped")
        return
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TurtleMaster.settings')
    # conn = sqlite3.connect('WC.db.sqlite')]
    dbsettings = settings.DATABASES['default']

    conn = psycopg2.connect(host=dbsettings["HOST"], database=dbsettings["NAME"],
                            user=dbsettings["USER"], password=dbsettings["PASSWORD"])
    cur = conn.cursor()

    if(drop_table == 'yes') :
        cur.execute('''
        DROP TABLE IF EXISTS TIME_SERIES_DATA_WORLD
        ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS TIME_SERIES_DATA_WORLD (
        id SERIAL PRIMARY KEY,
        province_state  TEXT,
        country_region  TEXT,
        last_update  DATE,
        confirmed  INTEGER,
        deaths  INTEGER,
        recovered  INTEGER,
        timestamp timestamp default current_timestamp,
        UNIQUE (province_state, last_update)
        )
    ''')
    num_line = 0
    fh = open(fname, 'r')
    csv_reader = csv.reader(fh)
    key_pos_dic = {}
    date_key_dic = {}
    for line in csv_reader:
        pieces = line
        if(pieces[0].endswith('UID') or pieces[0].endswith('Province/State')):
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
                date_key = re.search(r'(\d+(/|-){1}\d+(/|-){1}\d{2,4})',key)
                if date_key is not None :  date_key_dic[key] = index
                index += 1
            continue
        if(pieces[0] == 'Recovered'): continue

        country_region=pieces[key_pos_dic["country_region"]]
        province_state=pieces[key_pos_dic["province_state"]] or country_region

        for date_key in date_key_dic :
            last_update = date_key
            update_value = pieces[date_key_dic[date_key]]
            insert_sql='''INSERT INTO TIME_SERIES_DATA_WORLD (
            province_state,
            country_region,
            last_update,
            confirmed,
            deaths,
            recovered
           )
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (province_state, last_update) DO NOTHING
            '''

            insert_val=(
            province_state,
            country_region,
            last_update,
            "0",
            "0",
            "0"
           )
            cur.execute(insert_sql, insert_val)

            update_sql_stat='''UPDATE TIME_SERIES_DATA_WORLD SET
                {} = %s
                WHERE province_state = %s and last_update = %s::date
                RETURNING last_update
                '''.format(update_key)
            update_val=(
                update_value,
                province_state,
                last_update
            )

            cur.execute(update_sql_stat, update_val)

            num_line += 1
            print(num_line, " of lines has been processed", num_line, end='\r', flush=True)

    conn.commit()
    cur.close()
    print(num_line, " of lines has been processed")

def do_statistics_view_data(drop_table):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TurtleMaster.settings')
    # conn = sqlite3.connect('WC.db.sqlite')]
    dbsettings = settings.DATABASES['default']

    country_region_list = {
        "US" : '''
            SELECT
            max(last_update),
            sum(confirmed),
            sum(deaths),
            sum(recovered)
            FROM INFECTION_DATA_US_STATISTICS
            WHERE country_region = %s''',

        "China" : '''
            SELECT
            max(last_update),
            sum(confirmed),
            sum(deaths),
            sum(recovered)
            FROM INFECTION_DATA_WORLD_STATISTICS
            WHERE country_region = %s''',

        "World" : '''
            SELECT
            max(last_update),
            sum(confirmed),
            sum(deaths),
            sum(recovered)
            FROM INFECTION_DATA_WORLD_STATISTICS
            ''',

    }

    conn = psycopg2.connect(host=dbsettings["HOST"], database=dbsettings["NAME"],
                            user=dbsettings["USER"], password=dbsettings["PASSWORD"])
    cur = conn.cursor()
    if(drop_table == 'yes') :
        cur.execute('''
        DROP TABLE IF EXISTS VIEW_STATISTICS_DATA
        ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS VIEW_STATISTICS_DATA (
        id SERIAL PRIMARY KEY,
        country_region  TEXT,
        last_update  DATE,
        confirmed  INTEGER,
        deaths  INTEGER,
        recovered  INTEGER,
        timestamp timestamp default current_timestamp,
        UNIQUE (country_region)
        )
    ''')

    insert_query = '''
    INSERT INTO VIEW_STATISTICS_DATA (
            country_region,
            last_update,
            confirmed,
            deaths,
            recovered
           )
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (country_region) DO NOTHING'''

    update_query = '''
    UPDATE VIEW_STATISTICS_DATA SET (
            last_update,
            confirmed,
            deaths,
            recovered
            ) = (%s, %s, %s, %s)
            WHERE country_region = %s

    '''
    for country_region in country_region_list:
        last_update = date.today().strftime("%m/%d/%Y %H:%M:%S")
        confirmed = 0
        deaths = 0
        recovered = 0
        select_query = country_region_list[country_region]
        select_value = (
        country_region,
        )

        cur.execute(select_query,select_value)

        rows = cur.fetchall()
        for row in rows:
            last_update = row[0]
            confirmed += (int(row[1]) if row[1] is not None else 0)
            deaths += (int(row[2]) if row[2] is not None else 0)
            recovered += (int(row[3])  if row[3] is not None else 0)
        insert_value = (
            country_region,
            last_update,
            confirmed,
            deaths,
            recovered
        )
        cur.execute(insert_query,insert_value)
        update_value = (
            last_update,
            confirmed,
            deaths,
            recovered,
            country_region
        )
        print(update_value)
        cur.execute(update_query, update_value)
        conn.commit()

    cur.close()

def iterate_files(folder_path, data_type, drop_table):
    print("Iterate in  ", folder_path)
    for filename in sorted(os.listdir(folder_path)):
        fullpath=os.path.join(folder_path, filename)
        if not filename.startswith("_") and not filename.startswith(".") and filename.endswith(".csv"):
            try:
                if(data_type == "us"):
                    parser_us_data(fullpath, drop_table)
                if (data_type == "world"):
                    parser_world_data(fullpath, drop_table)
                if(data_type == "time_series"):
                    parser_time_series_data_us(fullpath, if_drop_table)
                    parser_time_series_data_global(fullpath, if_drop_table)

            except:
                track = traceback.format_exc()
                print(track)
                print(sys.exc_info()[0])
                quit()



default_folder=os.path.abspath(os.path.join(
    os.getcwd(), "../COVID-19/csse_covid_19_data/"))
us_data_folder="csse_covid_19_daily_reports_us"
world_data_folder="csse_covid_19_daily_reports"
time_series_folder = "csse_covid_19_time_series"

root_directory=input("Enter folder name: ")
if (len(root_directory) < 1): root_directory=default_folder
if_drop_table = input("Drop all tables?: [No/yes]")
us_data_full_path=os.path.join(root_directory, us_data_folder)
world_data_full_path = os.path.join(root_directory, world_data_folder)
time_series_data_full_path = os.path.join(root_directory, time_series_folder)
start_time = time.time()
iterate_files(us_data_full_path, "us", if_drop_table)
iterate_files(world_data_full_path, "world", if_drop_table)
iterate_files(time_series_data_full_path, "time_series", if_drop_table)
do_statistics_view_data(if_drop_table)
elapsed_time = time.time() - start_time
print("elapsed_time:", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
