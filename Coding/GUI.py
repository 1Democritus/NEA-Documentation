#import needed files
from featureEngineering import labels, features
import nn
#import needed modules
from tkinter import *
import string
import numpy
import psycopg2
import calendar, datetime
from dotenv import load_dotenv
load_dotenv(override=True)
PARAMETERS = os.getenv("PARAMETERS").split(",")
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase

#setting up accounts list for login validation
with psycopg2.connect(dbname = "logins", **PARAMETERS) as conn:
    conn.autocommit = True
    cursor = conn.cursor()
    query = "SELECT email, password FROM logindetails;"
    cursor.execute(query)
    accountDetails = cursor.fetchall()

class Interface:
    #open main menu of interface
    def __init__(self):
        self.screen = Tk()
        self.screen.geometry("500x500")
        self.screen.state("zoomed")
        self.screen.title("interfacePOC")

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
        self.loginMain = Label(self.screen, text = "Welcome back! Sign back in now.")
        self.loginMain.pack()
        self.emailLabel = Label(self.screen, text = "email")
        self.emailLabel.pack()
        self.emailText = Entry(self.screen)
        self.emailText.pack()
        self.passwordLabel = Label(self.screen, text = "password")
        self.passwordLabel.pack()
        self.passwordText = Entry(self.screen)
        self.passwordText.pack()
        self.loginButton = Button(self.screen, text = "Login", command = self.checkLogin)
        self.loginButton.pack()
        #add access codes later

    def checkLogin(self):
        email = self.emailText.get()
        password = self.passwordText.get()
        print(accountDetails)
        if (email, password) not in accountDetails:
            self.loginMain.config(text = "Wrong email or password")
        else:
            self.displayForm()
    
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
        elif not validEmailChecker(email):
            self.registryMain.config(text = "Not valid email. Please enter your actual email.")
        else:
            with psycopg2.connect(dbname = "logins", **PARAMETERS) as connect:
                connect.autocommit = True
                cursor = connect.cursor()
                query = '''
INSERT INTO logindetails(email, password, accesscode)
VALUES(%s, %s, )
'''
                cursor.execute(query, (email, password))
            self.displayForm()
        
    def displayForm(self):
        self.isFemale = False
        self.accountEmail = self.emailText.get()
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
        self.bodyacheButton = Button(self.screen, text = "body ache", command = lambda:self.changeSymptom(self.bodyache, self.bodyacheButton, "body ache"))
        self.bodyacheButton.grid(row = 1, column = 0)
        self.coughButton = Button(self.screen, text = "cough", command = lambda:self.changeSymptom(self.cough, self.coughButton, "cough"))
        self.coughButton.grid(row = 1, column = 1)
        self.shortnessbreathButton = Button(self.screen, text = "shortness of breath", command = lambda:self.changeSymptom(self.shortnessbreath, self.shortnessbreathButton, "shortness of breath"))
        self.shortnessbreathButton.grid(row = 1, column = 2)
        self.fatigueButton = Button(self.screen, text = "Fatigue", command = lambda: self.changeSymptom(self.fatigue, self.fatigueButton, "Fatigue"))
        self.fatigueButton.grid(row = 1, column = 3)
        self.feverButton = Button(self.screen, text = "Fatigue", command = lambda:self.changeSymptom(self.fever, self.feverButton, "Fever"))
        self.feverButton.grid(row = 2, column = 0)
        self.headacheButton = Button(self.screen, text = "Headache", command = lambda:self.changeSymptom(self.headache, self.headacheButton, "Headache"))
        self.headacheButton.grid(row = 2, column = 1)
        self.runnynoseButton = Button(self.screen, text = "Runny Nose", command = lambda:self.changeSymptom(self.runnynose, self.runnynoseButton, "Runny Nose"))
        self.runnynoseButton.grid(row = 2, column = 2)
        self.sorethroatButton = Button(self.screen, text = "Sore Throat", command = lambda:self.changeSymptom(self.sorethroat, self.sorethroatButton, "Sore Throat"))
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
        self.displayDates = Label(self.screen, height = 4, text = f"Following days aren't available: {self.unavailableDates}. With that in mind, enter your preferred date.")
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
            print(patientID, self.treatment, self.date)
            connection = psycopg2.connect(dbname = 'appointments', **PARAMETERS)
            connection.autocommit = True
            cursor = connection.cursor()
            statement = '''INSERT INTO APPOINTMENTS (AppointmentID, PatientID, DoctorID, TreatmentName, AppointmentDate, AppointmentTime, RoomNumber)
            VALUES (001, %s, 001, %s, %s, 13:15, 25);'''
            cursor.execute(statement, (patientID, self.treatment, self.date))
            connection.close()

            self.clearScreen()
            self.confirmation = Label(self.screen, text = "Done! We have scheduled your appointment. Click the button below to add the appointment to calendar. Otherwise, thank you for using our service!")
            self.confirmation.pack()
            self.calendarButton = Button(self.screen, text = "Add to Calendar", command = self.addToCalendar)
            self.calendarButton.pack()
        except Exception as e:
            print(e)
            self.appointmentConfirm.config(text = "Please ensure you've entered the date in the right format")
        
    def addToCalendar(self):
        pass

    def changeSymptom(self, symptom, button, symptomName):
        if symptom == 0:
            symptom = 1
            button.config(text = "Click if you made a mistake and don't have " + symptomName)
        else:
            symptom = 0
            button.config(text = symptomName)

    def storeDetails(self):
        try:
            self.heartrate = int(self.heartrateInput.get())
            self.age = int(self.ageInput.get())
            bloodpressure = self.bloodpressureInput.get().split("/")
            if len(bloodpressure) != 2:
                raise ValueError()
            self.systolic = int(bloodpressure[0])
            self.diastolic = int(bloodpressure[1])
            self.bodytemperature = int(self.bodytemperatureInput.get())
            self.oxygen = int(self.oxygenInput.get())
            self.isFemale = int(self.isFemale)
            self.displaySymptoms()
        except:
            self.formLabel.config(text = "Please ensure all data you've entered is in valid format")
    
    def changeGender(self):
        if self.isFemale:
            self.isFemale = False
            self.genderInput.config(text = "Press if you're a woman")
        else:
            self.isFemale = True
            self.genderInput.config(text = "Press if you're a man")
        
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
    
def validEmailChecker(email):
    validDomains = ["nhs.ac.uk", "denizati.tr", "gmail.com", "yahoo.com", "mcsoxford.org.uk"]
    emailContents = email.split("@")
    if len(emailContents) != 2:
        return False
    name, domain = emailContents[0], emailContents[1]
    for disallowedChar in ["/", "?", "!", "*", "(", ")"]:
        if disallowedChar in name:
            return False
    return domain in validDomains and name[0] not in [".", "_", "-"]

def getPredictions(details):
    #combine features in format of database and label it xtest=
    model = nn.DNN(learningRate = 0.01, columnSize = features.shape[0], outputSize = labels.shape[0])
    Oracle = nn.trainModel(model = model, epochCount = 200, label = labels, trainset = features)
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
    return dates

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
