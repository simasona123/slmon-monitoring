import sqlite3
import json


# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('slmon.db')

# Create a cursor object
cur = conn.cursor()
    
cur.execute('''
CREATE TABLE IF NOT EXISTS metadatas (
    id INTEGER PRIMARY KEY,
    staname TEXT UNIQUE,
    digitizer TEXT,
    ipaddr TEXT,
    lat REAL,
    long REAL
)
''')

conn.execute('PRAGMA foreign_keys = ON')

cur.execute('''
CREATE TABLE IF NOT EXISTS slmons (
    timestamp TEXT,
    sitename TEXT,
    timech TEXT,
    latency INTEGER,
    status TEXT,
    PRIMARY KEY (timestamp, sitename),
    FOREIGN KEY (sitename) REFERENCES metadatas (staname)
)
''')

cur.execute('DELETE FROM metadatas')

print('delete metadatas')

# Optionally, reset the auto-increment counter for the table
# cur.execute('DELETE FROM sqlite_sequence WHERE name="metadatas"')

with open('init.json', 'r') as file:
    data = json.load(file)

for site in data['features']:
    properties = site['properties']
    cur.execute('''
    INSERT INTO metadatas (staname, digitizer, ipaddr, lat, long) 
    VALUES (?, ?, ?, ?, ?)
    ''', (properties['sta'], properties['merkdgtz'], properties['ipaddr'], site['geometry']['coordinates'][0], site['geometry']['coordinates'][1]))
    print(properties['sta'])

conn.commit()
# Close the connection
conn.close()
