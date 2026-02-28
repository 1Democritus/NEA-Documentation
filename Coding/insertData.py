import psycopg2
import os
from dotenv import load_dotenv
load_dotenv(override=True)
PARAMETERS = os.getenv("PARAMETERS").split(",") #contains details needed to access the server
PARAMETERS = {"host": PARAMETERS[2], "user": PARAMETERS[0], "password": PARAMETERS[1]}
conn = psycopg2.connect(dbname = 'logins', **PARAMETERS)
conn.autocommit = True #every SQL query will be committed without requiring specific commits
cursor = conn.cursor()

def rollingHash(key, rollingPrime = 31, length = 101):
        hashSum = 0
        for i in range(len(key)):
            hashSum += ord(key[i]) * (rollingPrime ** i)
        return hashSum % length

accounts = [('c.akcabay@denizati.tr', 'boSSdhuraN', ''), ('mike.smith@nhs.ac.uk', 'mike1234', 'AP6QT#')]
for email, password, accessCode in accounts:
  password = rollingHash(password)
  accessCode = rollingHash(accessCode) if accessCode != '' else ''
  statement = 'INSERT INTO loginDetails VALUES(%s, %s, %s);'
  cursor.execute(statement, (email, password, accessCode))
conn.close()

conn = psycopg2.connect(dbname = 'appointments', **PARAMETERS)
conn.autocommit = True #every SQL query will be committed without requiring specific commits
cursor = conn.cursor()

cursor.execute('INSERT INTO Room VALUES(%s, %s);', (1,1))
cursor.execute('INSERT INTO Patient VALUES(%s, %s, %s, %s, %s);', ("CemAck001", "Cem", "Akcabay", "c.akcabay@denizati.tr", "09129358407"))
cursor.execute('INSERT INTO Doctor VALUES(%s, %s, %s, %s);', ("MikSmi001", "Mike", "Smith", "08410248536"))
