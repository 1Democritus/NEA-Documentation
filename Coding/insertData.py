import psycopg2
import os
from dotenv import load_dotenv
load_dotenv(override=True)
PARAMETERS = os.getenv("PARAMETERS").split(",") #contains details needed to access the server
PARAMETERS = {"host": PARAMETERS[2], "user": PARAMETERS[0], "password": PARAMETERS[1]}
connection = psycopg2.connect(dbname = 'logins', **PARAMETERS)
connection.autocommit = True #every SQL query will be committed without requiring specific commits
cursor = connection.cursor()

def rollingHash(key, rollingPrime = 31, length = 101):
        hashSum = 0
        for i in range(len(key)):
            hashSum += ord(key[i]) * (rollingPrime ** i)
        return hashSum % length

accounts = [('c.akcabay@denizati.tr', 'boSSdhuraN', ''), ('mike.smith@nhs.ac.uk', 'mike1234', 'AP6QT#')]
patient = [('CemAkc001','Cem', 'Akcabay', '')]
for email, password, accessCode in accounts:
  password = rollingHash(password)
  accessCode = rollingHash(accessCode) if accessCode != '' else ''
  statement = 'INSERT INTO loginDetails VALUES(%s, %s, %s)'
  cursor.execute(statement, (email, password, accessCode))
conn.close()
