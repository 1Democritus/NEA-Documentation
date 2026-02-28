#import needed files
from featureEngineering import labels, features
import nn
#import needed modules
from tkinter import *
import string
import numpy
import psycopg2
import calendar, datetime
import caldav
import re
import os
from dotenv import load_dotenv
load_dotenv(override=True)
PARAMETERS = os.getenv("PARAMETERS").split(",")
PARAMETERS = {"host": PARAMETERS[2], "user": PARAMETERS[0], "password": PARAMETERS[1]}
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase

#setting up accounts list for login validation
with psycopg2.connect(dbname = "logins", **PARAMETERS) as conn:
    conn.autocommit = True
    cursor = conn.cursor()
    query = "SELECT * FROM logindetails;"
    cursor.execute(query)
    accountDetails = cursor.fetchall()

class Interface:
    #open main menu of interface
    def __init__(self):
        self.screen = Tk()
        self.screen.geometry("500x500")
        self.screen.state("zoomed")
        self.screen.title("interfacePOC")

        self.accountDictionary = HashTable()
        for [email, password, accessCode] in accountDetails:
            self.accountDictionary.add(email, password, accessCode)

        self.registryLabel = Label(self.screen, text = "Welcome back! Please sign in or create a new account so that we can help with your health concerns")
        self.registryLabel.pack()
        self.loginButton = Button(self.screen, text = "SIGN IN", command = self.login)
        self.loginButton.pack()
        self.registerButton = Button(self.screen, text = "REGISTER", command = self.register)
        self.registerButton.pack()

    #function for transitioning between screens
    def clearScreen(self):
        for widget in self.screen.winfo_children():
            widget.destroy()

    def login(self):
        self.clearScreen()
        self.loginMain = Label(self.screen, text = "Welcome back! Sign back in now. If you aren't staff, leave access code empty.")
        self.loginMain.pack()
        self.emailLabel = Label(self.screen, text = "email")
        self.emailLabel.pack()
        self.emailText = Entry(self.screen)
        self.emailText.pack()
        self.passwordLabel = Label(self.screen, text = "password")
        self.passwordLabel.pack()
        self.passwordText = Entry(self.screen)
        self.passwordText.pack()
        self.accesscodeLabel = Label(self.screen, text = "Access code")
        self.accesscodeLabel.pack()
        self.accesscodeText = Entry(self.screen)
        self.accesscodeText.pack()
        self.loginButton = Button(self.screen, text = "Login", command = self.checkLogin)
        self.loginButton.pack()

    def checkLogin(self):
        email = self.emailText.get()
        password = HashTable.rollingHash(self.passwordText.get())
        accessCode = 0
        DBresults = self.accountDictionary.search(email)
        accessCode = HashTable.rollingHash(self.accesscodeText.get())
        if DBresults == None:
            self.loginMain.config("email doesn't exist")
        else:
            DBpassword = int(DBresults[0])
            DBaccessCode = int(DBresults[1])
            if (password != DBpassword or accessCode != DBaccessCode) and DBaccessCode == 0:
                self.loginMain.config(text = "Wrong password")
            elif (password != DBpassword or accessCode != DBaccessCode) and DBaccessCode != 0:
                self.loginMain.config(text = "Wrong password or access code")
            elif accessCode == 0:
                self.displayForm()
            else:
                self.staffMenu()
    
    def register(self):
        self.clearScreen()
        self.registryMain = Label(self.screen, text = "Please put your details here so that we can get started")
        self.registryMain.pack()
        self.emailLabel = Label(self.screen, text = "email")
        self.emailLabel.pack()
        self.emailText = Entry(self.screen)
        self.emailText.pack()
        self.passwordLabel = Label(self.screen, text = "password")
        self.passwordLabel.pack()
        self.passwordText = Entry(self.screen)
        self.passwordText.pack()
        self.registerButton = Button(self.screen, text = "Register account", command = self.checkRegistry)
        self.registerButton.pack()

    def checkRegistry(self):
        email = self.emailText.get()
        password = self.passwordText.get()
        if not strongPasswordChecker(password):
            self.registryMain.config(text = "Password not strong enough. Please choose a different password.")
        elif not validEmailChecker(email, self.accountDictionary):
            self.registryMain.config(text = "Not valid email. Please enter your actual email.")
        else:
            self.newEmail = email
            self.newPassword = str(HashTable.rollingHash(password))
            self.enterDatabaseDetails()
    
    def enterDatabaseDetails(self):
        self.clearScreen()
        self.newRegDetails = Label(self.screen, text = "Welcome to our app! Please enter these details so that we can make appointments for you in the future!")
        self.newRegDetails.pack()
        self.forenameLabel = Label(self.screen, text = "Enter your name please")
        self.forenameLabel.pack()
        self.forename = Entry(self.screen)
        self.forename.pack()
        self.surnameLabel = Label(self.screen, text = "Enter your surname")
        self.surnameLabel.pack()
        self.surname = Entry(self.screen)
        self.surname.pack()
        self.telephoneLabel = Label(self.screen, text = "Enter your phone")
        self.telephoneLabel.pack()
        self.telephone = Entry(self.screen)
        self.telephone.pack()
        self.registryConfirmButton = Button(self.screen, text = "Submit details", command = self.storeNewAccount)
        self.registryConfirmButton.pack()

    def storeNewAccount(self):
        forename = self.forename.get()
        surname = self.surname.get()
        telephone = self.telephone.get()
        if not telephone.isnumeric() or len(telephone) != 11:
            self.telephoneLabel.config(text = "Please enter a valid telephone number of length 11")
        elif not surname.isalpha():
            self.surnameLabel.config(text = "Enter your actual surname")
        elif not forename.isalpha():
            self.forenameLabel.config(text = "Please only enter your first name; middle names aren't accepted")
        else:
            with psycopg2.connect(dbname = 'logins', **PARAMETERS) as conn1:
                conn1.autocommit = True
                cursor = conn1.cursor()
                cursor.execute('''
                INSERT INTO loginDetails(email, password, accesscode)
                VALUES (%s, %s, '0');
''', (self.newEmail, self.newPassword))
            with psycopg2.connect(dbname = 'appointments', **PARAMETERS) as conn2:
                conn2.autocommit = True
                cursor = conn2.cursor()
                id = forename[0:4] + surname[0:4] + telephone[0:4]
                statement = '''
INSERT INTO Patient(PatientID, Forename, Surname, telephoneNo, email)
VALUES (%s,%s,%s,%s,%s);
'''
                cursor.execute(statement, (id, forename, surname, telephone, self.newEmail))
            self.displayForm()
            
        
    def displayForm(self):
        self.isFemale = False
        try:
            self.accountEmail = self.emailText.get()
        except:
            self.accountEmail = self.newEmail
        self.clearScreen()
        self.formLabel = Label(self.screen, text = "Please enter your details so the Oracle can give the most accurate predictions")
        self.formLabel.grid(row = 0, column = 1)
        self.heartrateLabel = Label(self.screen, text = "Enter heartrate")
        self.heartrateLabel.grid(row = 1, column = 0)
        self.heartrateInput = Entry(self.screen)
        self.heartrateInput.grid(row = 2, column = 0)
        self.ageLabel = Label(self.screen, text = "Enter age")
        self.ageLabel.grid(row = 1, column = 1)
        self.ageInput = Entry(self.screen)
        self.ageInput.grid(row = 2, column = 1)
        self.bloodpressureLabel = Label(self.screen, text = "Enter your blood pressure (in the format systolic/diastolic)")
        self.bloodpressureLabel.grid(row = 1, column = 2)
        self.bloodpressureInput = Entry(self.screen)
        self.bloodpressureInput.grid(row = 2, column = 2)
        self.bodytemperatureLabel = Label(self.screen, text = "Body Temperature (Celcius)")
        self.bodytemperatureLabel.grid(row = 3, column = 0)
        self.bodytemperatureInput = Entry(self.screen)
        self.bodytemperatureInput.grid(row = 4, column = 0)
        self.genderInput = Button(self.screen, text = "Press if you're a woman", command = self.changeGender)
        self.genderInput.grid(row = 4, column = 1)
        self.oxygenLabel = Label(self.screen, text = "Enter Oxygen saturation %")
        self.oxygenLabel.grid(row = 3, column = 2)
        self.oxygenInput = Entry(self.screen)
        self.oxygenInput.grid(row = 4, column = 2)
        self.detailsButton = Button(self.screen, text = "Click here to submit", command = self.storeDetails)
        self.detailsButton.grid(row = 5, column = 1)
    
    def displaySymptoms(self):
        self.bodyache = 0
        self.cough = 0
        self.shortnessbreath = 0
        self.fatigue = 0
        self.fever = 0
        self.headache = 0
        self.runnynose = 0
        self.sorethroat = 0
        self.clearScreen()
        self.symptomLabel = Label(self.screen, text = "Please click on the symptoms that you have experienced")
        self.symptomLabel.grid(row = 0, column = 1)
        self.bodyacheButton = Button(self.screen, text = "body ache", command = lambda:self.changeSymptom(self.bodyacheButton, "body ache", "bodyache"))
        self.bodyacheButton.grid(row = 1, column = 0)
        self.coughButton = Button(self.screen, text = "cough", command = lambda:self.changeSymptom(self.coughButton, "cough", "cough"))
        self.coughButton.grid(row = 1, column = 1)
        self.shortnessbreathButton = Button(self.screen, text = "shortness of breath", command = lambda:self.changeSymptom(self.shortnessbreathButton, "shortness of breath", "shortnessbreath"))
        self.shortnessbreathButton.grid(row = 1, column = 2)
        self.fatigueButton = Button(self.screen, text = "Fatigue", command = lambda: self.changeSymptom(self.fatigueButton, "Fatigue", "fatigue"))
        self.fatigueButton.grid(row = 1, column = 3)
        self.feverButton = Button(self.screen, text = "Fever", command = lambda:self.changeSymptom(self.feverButton, "Fever", self.fever))
        self.feverButton.grid(row = 2, column = 0)
        self.headacheButton = Button(self.screen, text = "Headache", command = lambda:self.changeSymptom(self.headacheButton, "Headache", "headache"))
        self.headacheButton.grid(row = 2, column = 1)
        self.runnynoseButton = Button(self.screen, text = "Runny Nose", command = lambda:self.changeSymptom(self.runnynoseButton, "Runny Nose", "runnynose"))
        self.runnynoseButton.grid(row = 2, column = 2)
        self.sorethroatButton = Button(self.screen, text = "Sore Throat", command = lambda:self.changeSymptom(self.sorethroatButton, "Sore Throat", "sorethroat"))
        self.sorethroatButton.grid(row = 2, column = 3)
        self.symptomSubmit = Button(self.screen, text = "Click here to submit", command = self.readyPrediction)
        self.symptomSubmit.grid(row = 3, column = 1)
    
    def readyPrediction(self):
        self.clearScreen()
        details = numpy.array([self.age, self.isFemale, self.heartrate, self.bodytemperature, self.oxygen, self.systolic, self.diastolic, self.bodyache, self.cough, self.shortnessbreath, self.fatigue, self.fever, self.headache, self.runnynose, self.sorethroat])
        self.disease = getPredictions(details)
        self.displayOptions()
        #prepare to pass details into the machine

    def displayOptions(self):
        if self.disease == "Healthy":
            Oracle = Label(self.screen, text = "Good news, you don't have a disease! You should rest for a couple days, and then you should be fine. Thank you for using this service!")
            Oracle.pack()
        else:
            self.Oracle = Label(self.screen, text = "You have the disease " + self.disease)
            self.Oracle.pack()
            self.month = Entry(self.screen)
            self.month.pack()
            self.monthButton = Button(self.screen, text = "Display possible dates in above entered month", command = self.returnDates)
            self.monthButton.pack()

    def returnDates(self):
        month = self.month.get()
        self.unavailableDates = SQLCall(month, self.disease)
        self.displayDates = Label(self.screen, height = 10, wraplength = 400, text = f"Following days aren't available: {self.unavailableDates}. With that in mind, enter your preferred date.")
        self.displayDates.pack()
        self.preferredTime = Entry(self.screen)
        self.preferredTime.pack()
        self.appointmentConfirm = Button(self.screen, text = "Confirm Appointment, please enter your date in the format dd/mm/yyyy", command = self.confirmAppointment)
        self.appointmentConfirm.pack()
    
    def confirmAppointment(self):
        try:
            patientID, self.treatment = getDetails(self.accountEmail, self.disease)
            self.date = self.preferredTime.get()
            if self.date in self.unavailableDates:
                raise ValueError()
            connection = psycopg2.connect(dbname = 'appointments', **PARAMETERS)
            connection.autocommit = True
            cursor = connection.cursor()
            id = None
            count = 1
            statement = '''INSERT INTO Appointment (AppointmentID, PatientID, DoctorID, TreatmentName, AppointmentDate, AppointmentTime, RoomNumber)
            VALUES (%s, %s, 'MikSmi001', %s, %s, '13:15:00', 1);'''
            while id is None: #subroutine to generate unique id for every appointment
                try:
                    id = patientID + 'Kooth' + str(count)
                    cursor.execute(statement, (id, patientID, self.treatment, self.date))
                except:
                    id = None
                    count += 1

            connection.close()

            self.clearScreen()
            self.confirmation = Label(self.screen, text = "Done! We have scheduled your appointment. Click the button below to add the appointment to calendar. Otherwise, thank you for using our service!")
            self.confirmation.pack()
            self.calendarButton = Button(self.screen, text = "Add to Calendar", command = self.addToCalendar)
            self.calendarButton.pack()
        except Exception as e:
            self.appointmentConfirm.config(text = "Please ensure you've entered the date in the right format")
        
    def addToCalendar(self):
        self.screen.withdraw()
        popup = CalendarPopup(self.screen)
        self.screen.wait_window(popup) #waits to proceed until popup window is destroyed
        username, password = popup.result
        dateValues = self.date.split("/")
        year, month, day = int(dateValues[2]), int(dateValues[1]), int(dateValues[0])
        try:
            client = caldav.DAVClient(url = "https://caldav.icloud.com/", username = username, password = password)
            myCalendar = client.principal().calendars()[0]
            myCalendar.save_event(
            dtstart = datetime.datetime(year, month, day, 6, 0),
            dtend = datetime.datetime(year, month, day, 7, 0),
            summary = "ORACLE APPOINTMENT"
        )
            finalMsg = "Appointment scheduled, see you then!"
        except Exception as e:
            finalMsg = "Error", f"Sorry, something went wrong while adding to calendar: {e}"
        finally:
            self.screen.deiconify()
            self.clearScreen()
            self.finalLabel = Label(text = finalMsg)
            self.finalLabel.pack()

    def changeSymptom(self, button, symptomName, symptom):
        textContent = button.cget('text') #acquires text variable from the button
        if textContent == symptomName:
            button.config(text = "Click if you made a mistake and don't have " + symptomName)
            setattr(self, symptom, 1) #if changed the variable locally change wouldn't happen outside of subroutine
        else:
            button.config(text = symptomName)
            setattr(self, symptom, 0)

    def storeDetails(self):
        try:
            self.heartrate = float(self.heartrateInput.get())
            if self.heartrate < 40 or self.heartrate > 240:
                raise ValueError("Please don't mock our application by entering a fake heartrate")
            elif self.heartrate > 130:
                raise ValueError("Please enter your resting heartrate; entering your heartrate after exercise might reduce accuracy")
            self.age = int(self.ageInput.get())
            if self.age < 0 or self.age > 120:
                raise ValueError("Please enter your actual age")
            bloodpressure = self.bloodpressureInput.get().split("/")
            if len(bloodpressure) != 2:
                raise AttributeError("Blood pressure should have two values separated by a /")
            self.systolic = int(bloodpressure[0])
            self.diastolic = int(bloodpressure[1])
            self.bodytemperature = int(self.bodytemperatureInput.get())
            if self.bodytemperature < 25 or self.bodytemperature > 45:
                raise ValueError("Please enter a valid temperature between 25 and 45 degrees Celsius")
            self.oxygen = int(self.oxygenInput.get())
            if self.oxygen < 70 or self.oxygen > 100:
                raise ValueError("Your oxygen saturation is either immediately fatal or not possible. Please enter your actual saturation")
            self.isFemale = int(self.isFemale)
            self.displaySymptoms()
        except Exception as e:
            self.formLabel.config(text = e)

    def changeGender(self):
        if self.isFemale:
            self.isFemale = False
            self.genderInput.config(text = "Press if you're a woman")
        else:
            self.isFemale = True
            self.genderInput.config(text = "Press if you're a man")

    def staffMenu(self):
        self.clearScreen()
        self.mainLabel = Label(self.screen, text = "staff menu")
        self.mainLabel.pack()
        self.addButton = Button(self.screen, text = "Add appointment", command = self.addAppointment)
        self.addButton.pack()
        self.removeButton = Button(self.screen, text = "Remove appointment", command = self.removeAppointment)
        self.removeButton.pack()

    def removeAppointment(self):
        self.clearScreen()
        conn = psycopg2.connect(dbname = 'appointments', **PARAMETERS)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute('''SELECT AppointmentID, PatientID, DoctorID, AppointmentDate FROM Appointment;''')
        self.appointments = cursor.fetchall()
        self.listOfAppointments = Label(self.screen, height = 10, wraplength = 400, text = f"Here are all the appointments on the database, please enter the id of the one you want to remove: {self.appointments}")
        self.listOfAppointments.pack()
        self.removedID = Entry(self.screen)
        self.removedID.pack()
        self.removeAppointmentButton = Button(self.screen, text = "Remove Button", command = lambda: self.removeSQL(cursor))
        self.removeAppointmentButton.pack()
        self.returnStaffButton = Button(self.screen, text = "Return to Menu", command = lambda: (conn.close(), self.staffMenu()))
        self.returnStaffButton.pack()

    def removeSQL(self, cursor):
        ID = self.removedID.get()
        try:
            cursor.execute('''
        DELETE FROM Appointment WHERE AppointmentID = %s;
                       ''', (ID,))
            if cursor.rowcount == 0: #meaning no data was actually removed
                raise ValueError()
            self.removeAppointmentButton.config(text = "Last request to remove appointment was successful")
            for appointment in self.appointments:
                if appointment[0] == ID:
                    self.appointments.remove(appointment)
            self.listOfAppointments.config(text = f"Here are all the appointments on the database, please enter the id of the one you want to remove: {self.appointments}")
        except:
            self.removeAppointmentButton.config(text = 'The appointment you want to remove does not exist')
    
    def addAppointment(self):
        conn = psycopg2.connect(dbname = 'appointments', **PARAMETERS)
        conn.autocommit = True
        cursor = conn.cursor()
        self.clearScreen()
        self.addMenu = Label(self.screen, text = "Please enter the details of your appointment")
        self.addMenu.grid(row = 0, column = 2)
        self.STAFFmeetingIDLabel = Label(self.screen, text = "Meeting ID")
        self.STAFFmeetingIDLabel.grid(row = 1, column = 0)
        self.STAFFmeetingID = Entry(self.screen)
        self.STAFFmeetingID.grid(row = 2, column = 0)
        self.STAFFdoctorIDLabel = Label(self.screen, text = "Doctor ID")
        self.STAFFdoctorIDLabel.grid(row = 1, column = 1)
        self.STAFFdoctorID = Entry(self.screen)
        self.STAFFdoctorID.grid(row = 2, column = 1)
        self.STAFFpatientIDLabel = Label(self.screen, text = "Patient ID")
        self.STAFFpatientIDLabel.grid(row = 1, column = 2)
        self.STAFFpatientID = Entry(self.screen)
        self.STAFFpatientID.grid(row = 2, column = 2)
        self.STAFFtreatmentLabel = Label(self.screen, text = "Treatment Name")
        self.STAFFtreatmentLabel.grid(row = 1, column = 3)
        self.STAFFtreatment = Entry(self.screen)
        self.STAFFtreatment.grid(row = 2, column = 3)
        self.STAFFdateLabel = Label(self.screen, text = "Date, in the format dd/mm/yyyy")
        self.STAFFdateLabel.grid(row = 1, column = 4)
        self.STAFFdate = Entry(self.screen)
        self.STAFFdate.grid(row = 2, column = 4)
        self.STAFFtimeLabel = Label(self.screen, text = "Time, in the format hh:mm:ss")
        self.STAFFtimeLabel.grid(row = 3, column = 1)
        self.STAFFtime = Entry(self.screen)
        self.STAFFtime.grid(row = 4, column = 1)
        self.STAFFroomLabel = Label(self.screen, text = "Room Number")
        self.STAFFroomLabel.grid(row = 3, column = 3)
        self.STAFFroom = Entry(self.screen)
        self.STAFFroom.grid(row = 4, column = 3)
        self.STAFFaddAppointment = Button(self.screen, text = "Add appointment", command = lambda: self.addSQL(cursor))
        self.STAFFaddAppointment.grid(row = 3, column = 2)
        self.STAFFreturnToMenu = Button(self.screen, text = "Return to main menu", command = lambda: (conn.close(), self.staffMenu()))
        self.STAFFreturnToMenu.grid(row = 4, column = 2)
    
    def addSQL(self, cursor):
        try:
            appointmentID = self.STAFFmeetingID.get()
            patientID = self.STAFFpatientID.get()
            doctorID = self.STAFFdoctorID.get()
            treatment = self.STAFFtreatment.get()
            date = self.STAFFdate.get()
            time = self.STAFFtime.get()
            room = self.STAFFroom.get()
            cursor.execute('''
INSERt INTO Appointment (AppointmentID, PatientID, DoctorID, TreatmentName, AppointmentDate, AppointmentTime, RoomNumber)
VALUES (%s, %s, %s, %s, %s, %s, %s);''', 
(appointmentID, patientID, doctorID, treatment, date, time, room))
        except:
            self.addMenu.config(text = "Either you've already added this appointment or some of the data is in the wrong format")
    
class CalendarPopup(Toplevel):
    def __init__(self, mainScreen):
        super().__init__(mainScreen) #derives basic window structure from the main screen's features
        self.labelUsername = Label(self, text = "Enter calendar username: ")
        self.entryUsername = Entry(self)
        self.labelPassword = Label(self, text = "Enter calendar password: ")
        self.entryPassword = Entry(self, show = "*") #to hide my actual password
        self.labelUsername.pack()
        self.entryUsername.pack()
        self.labelPassword.pack()
        self.entryPassword.pack()
        self.submitButton = Button(self, text = "Submit values", command = self.submitValues)
        self.submitButton.pack()
    
    def submitValues(self):
        self.result = (self.entryUsername.get(), self.entryPassword.get())
        self.destroy()

class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.table = [[] for i in range(self.size)]

    def add(self, email, passwordHashed, accessCodeHashed):
        index = self.rollingHash(email)
        self.table[index].append([email, (passwordHashed, accessCodeHashed)])

    def search(self, email):
        idx = self.rollingHash(email)
        for pair in self.table[idx]:
            if pair[0] == email:
                return pair[1]
        return None

    @staticmethod
    def rollingHash(key, rollingPrime = 31, length = 101):
        hashSum = 0
        for i in range(len(key)):
            hashSum += ord(key[i]) * (rollingPrime ** i)
        return hashSum % length
        
#general functions that don't need parameters
def strongPasswordChecker(password):
    checklist = [False, False, False, False, False]
    if len(password) >= 8:
        checklist[0] = True
    for k in password:
        if k in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            checklist[1] = True
        elif k in UPPERCASE:
            checklist[3] = True
        elif k in LOWERCASE:
            checklist[2] = True
        elif k in ["?", "!", "$", "£", "#", "@", "(", ")", "*", ".", "%"]:
            checklist[4] = True
    return False not in checklist
    
def validEmailChecker(email, accountDictionary):
    validDomains = ["nhs\.ac\.uk", "denizati\.tr", "gmail\.com", "yahoo\.com", "mcsoxford\.org\.uk"]

    domainPattern = "|".join([domain for domain in validDomains])

    #define the full regular expression
    #use rf instead of just f to signal to python that nothing inside this string is a special command
    validExpression = rf"^[^._\-\/?!*()@][^/?!*()@]*@({domainPattern})$"

    return re.fullmatch(validExpression, email, re.IGNORECASE) and accountDictionary.search(email) == None

def getPredictions(details):
    #combine features in format of database and label it xtest=
    model = nn.DNN(learningRate = 0.001, columnSize = features.shape[0], hiddenSize = 50, outputSize = labels.shape[0])
    Oracle = nn.trainModel(model = model, epochCount = 5000, label = labels, trainset = features)
    evaluation = Oracle.feedForward(details.reshape(-1, 1))    
    prediction = numpy.argmax(evaluation[3], axis = 0)
    conversion = {0: "Healthy", 1: "Bronchitis", 2: "Flu", 3: "Cold", 4: "Pneumonia"}
    return conversion[prediction[0]]

def SQLCall(month, disease):
    month = month.lower()
    monthConversion = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}
    month = monthConversion[month]
    range = calendar.monthrange(2025, month)[1]
    monthFirst = datetime.date(2025, month, 1)
    monthLast = datetime.date(2025, month, range)
    sqlText = f"""
SELECT AppointmentDate FROM Appointment, LinkedCondition
WHERE AppointmentDate >= %s AND AppointmentDate <= %s AND LinkedCondition.TreatmentName = Appointment.TreatmentName AND LinkedCondition.ConditionName = %s
ORDER BY AppointmentDate ASC;
"""
    connection = psycopg2.connect(dbname = "appointments", **PARAMETERS)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(sqlText, (monthFirst, monthLast, disease))
    dates = cursor.fetchall()
    connection.close()
    return [str(date) for date in dates]

def getDetails(email, disease):
    connection = psycopg2.connect(dbname = 'appointments', **PARAMETERS)
    connection.autocommit = True
    cursor = connection.cursor()
    emailStatement = '''SELECT PatientID FROM Patient WHERE
email = %s;
'''
    cursor.execute(emailStatement, (email, ))
    patientID = cursor.fetchone()
    diseaseStatement = '''SELECT TreatmentName FROM LinkedCondition WHERE
ConditionName = %s;    '''
    cursor.execute(diseaseStatement, (disease, ))
    treatmentName = cursor.fetchone()
    connection.close()
    return patientID[0], treatmentName[0] #since SQL results are always returned as a list

nhsInterface = Interface()
nhsInterface.screen.mainloop()
