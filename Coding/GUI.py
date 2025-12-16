from tkinter import *
from nnTrain import predictorModel as Oracle
import string
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase

#setting up accounts list for login validation
accountFile = open("accountsDemo.txt", "r")
accountDetails = []
line = accountFile.readline()
while line != "":
    accountDetails.append(line.split(" "))
    line = accountFile.readline()
accountFile.close()

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
        if [email, password] not in accountDetails:
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
            with open("accountsDemo.txt", "a") as file:
                file.writelines(email + " " + password + "\n")
                file.close()
            self.displayForm()
        
    def displayForm(self):
        self.clearScreen()
        pass
#general functions that don't need parameters
def strongPasswordChecker(password):
    print(password)
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
    validDomains = ["nhs.ac.uk", ""]
    emailContents = email.split("@")
    if len(emailContents) != 2:
        return False
    name, domain = emailContents[0], emailContents[1]
    for disallowedChar in ["/", "?", "!", "*", "(", ")"]:
        if disallowedChar in name:
            return False
    return domain in validDomains and name[0] not in [".", "_", "-"]
        

nhsInterface = Interface()
nhsInterface.screen.mainloop()
