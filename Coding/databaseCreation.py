import psycopg2
from databaseParameters import databaseParameters #contains values required to connect to server
connection = psycopg2.connect(dbname = 'postgres', **databaseParameters)
connection.autocommit = True #every SQL query will be committed without requiring specific commits
cursor = connection.cursor()
loginScript = 'CREATE DATABASE logins'
appointmentScript = 'CREATE DATABASE appointments'
cursor.execute(loginScript)
cursor.execute(appointmentScript)

#have to close and reopen a connection to the new database
cursor.close()
connection.close()

connection = psycopg2.connect(dbname = 'logins', **databaseParameters)
connection.autocommit = True
cursor = connection.cursor()

query = '''CREATE TABLE loginDetails (
email VARCHAR(40) PRIMARY KEY,
password VARCHAR(40) NOT NULL,
accesscode VARCHAR(15)
) '''

cursor.execute(query)
cursor.close()
connection.close()

#now repeat with appointment database
connection = psycopg2.connect(dbname = 'appointments', **databaseParameters)
connection.autocommit = True
cursor = connection.cursor()
appointmentQuery = '''
