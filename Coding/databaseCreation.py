import psycopg2
from dotenv import load_dotenv
load_dotenv(override=True)
PARAMETERS = os.getenv("PARAMETERS").split(",") #contains details needed to access the server
connection = psycopg2.connect(dbname = 'postgres', **PARAMETERS)
connection.autocommit = True #every SQL query will be committed without requiring specific commits
cursor = connection.cursor()
loginScript = 'CREATE DATABASE logins'
appointmentScript = 'CREATE DATABASE appointments'
cursor.execute(loginScript)
cursor.execute(appointmentScript)

#have to close and reopen a connection to the new database
cursor.close()
connection.close()

connection = psycopg2.connect(dbname = 'logins', **PARAMETERS)
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
connection = psycopg2.connect(dbname = 'appointments', **PARAMETERS)
connection.autocommit = True
cursor = connection.cursor()

treatmentQuery = '''CREATE TABLE Treatment(
TreatmentName VARCHAR(40) PRIMARY KEY,
TreatmentType VARCHAR(20) NOT NULL,
TreatmentHourDuration INT NOT NULL
)'''

conditionQuery = '''CREATE TABLE ConditionDetails(
ConditionName VARCHAR(40) PRIMARY KEY,
ConditionType VARCHAR(20) NOT NULL,
Severity VARCHAR(15) NOT NULL,
Contagiousness VARCHAR(15) NOT NULL
)'''

linkconditionQuery = '''CREATE TABLE LinkedCondition(
ConditionName VARCHAR(40) REFERENCES ConditionDetails(ConditionName),
TreatmentName VARCHAR(40) REFERENCES Treatment(TreatmentName),
PRIMARY KEY (ConditionName, TreatmentName)
)'''

doctorQuery = '''CREATE TABLE Doctor(
DoctorID VARCHAR(20) PRIMARY KEY,
DoctorName VARCHAR(15) NOT NULL,
Surname VARCHAR(15) NOT NULL,
TelephoneNo CHAR(11) NOT NULL
)'''

customerQuery = '''CREATE TABLE Patient(
PatientID VARCHAR(20) PRIMARY KEY,
Forename VARCHAR(15) NOT NULL,
Surname VARCHAR(15) NOT NULL,
Email VARCHAR(30) NOT NULL,
TelephoneNo CHAR(11) NOT NULL
)'''

roomQuery = '''CREATE TABLE Room(
RoomNumber INT PRIMARY KEY,
RoomFloor INT NOT NULL
)'''

appointmentQuery = '''CREATE TABLE Appointment(
AppointmentID VARCHAR(20) PRIMARY KEY,
PatientID VARCHAR(20) REFERENCES Patient(PatientID),
DoctorID VARCHAR(20) REFERENCES Doctor(DoctorID),
TreatmentName VARCHAR(40) REFERENCES Treatment(TreatmentName),
AppointmentDate DATE NOT NULL,
AppointmentTime TIME NOT NULL,
RoomNumber INT REFERENCES Room(RoomNumber)
)'''

queries = [treatmentQuery, conditionQuery, linkconditionQuery, doctorQuery, customerQuery, roomQuery, appointmentQuery]
for query in queries:
  cursor.execute(query)
cursor.close()
connection.close()
