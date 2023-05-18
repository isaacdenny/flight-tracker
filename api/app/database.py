import time

import psycopg2

time.sleep(10)
connection = None

try:
    connection = psycopg2.connect(
        dbname="flighttracker", host="db", user="ADMIN", password="PASSWORD"
    )
    connection.autocommit = True
    print("Established connection with database")
except Exception as e:
    print("Unable to connect to database!")
    print(f"The error '{e}' occurred!")
