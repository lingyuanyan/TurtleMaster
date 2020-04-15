import sqlite3

conn = sqlite3.connect('WC.db.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS INFECTION_DATA (
    province_state  TEXT PRIMARY KEY UNIQUE,
    country_region  TEXT,
    last_update  DATE,
    confirmed  INTEGER,
    deaths  INTEGER,
    lat  DOUBLE,
    long_  DOUBLE,
    recovered  INTEGER,
    active  INTEGER,
    FIPS  INTEGER,
    incident_rate  DOUBLE,
    people_tested  INTEGER,
    people_hospitalized  INTEGER,
    mortality_rate  DOUBLE,
    UID LONG,
    ISO3 TEXT,
    testing_rate  DOUBLE,
    hospitalization_rate  DOUBLE
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
    last_update = pieces[2]
    confirmed = pieces[3]
    deaths = pieces[4]
    lat = pieces[5]
    long_ = pieces[6]
    recovered = pieces[7]
    active = pieces[8]
    FIPS = pieces[9]
    incident_rate = pieces[10]
    people_tested = pieces[11]
    people_hospitalized = pieces[12]
    mortality_rate = pieces[13]
    UID = pieces[14]
    ISO3 = pieces[15]
    testing_rate = pieces[16]
    hospitalization_rate = pieces[17]

    insert_sql = '''INSERT INTO INFECTION_DATA (
        province_state, 
        country_region, 
        last_update, lat, 
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
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

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

    cur.execute(insert_sql, insert_val)

    conn.commit()

cur.close()
