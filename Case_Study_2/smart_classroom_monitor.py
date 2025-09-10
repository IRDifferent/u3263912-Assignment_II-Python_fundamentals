#Stephen James | u3263912 | 09/09/2025 | Smart Classroom Monitor

#Allows for timestamps to be used for tracking room temperatures
#Have commented as per the Assignment instructions, but if you want to see it in action uncomment all the time stuff (marked with ###)
#import datetime

roomState = {
    "projector_state" : bool,
    "computer_state": bool,
    "capacity" : 0,
    "class_unit" : str
    }
timeLog = [] #(time logging)
tempLog = [] #(temp logging)

cardNumber = 0

studentCards = { #Student card numbers
    "33331" : "Stephen James",
    "33332" : "Jane Doe",
    "33333" : "Sabine O'Connor"
    }
adminCards = { #Card numbers of those with admin access
    "00001" : "Joe Bloggs",
    "00002" : "John Smith"
    }
teacherCards = { #Teacher card numbers - nested dict so that the course they teach can be applied to the room (roomstate{"class_unit"})
    "11111" : {"Julio Romero" : "Intro to IT - Lecture"},
    "11112" : {"Nipuni Wijesinghe" : "Intro to IT - Tutorial"},
    "11113" : {"Nishant Jagannath" : "Intro to Network Engineering - Lecture"},
    "11114" : {"Maddie Wong" : "Intro to Network Engineering - Tutorial"}
    }
attendance = [] #Attendance log
lecturer = "Nil"

#Prints the temperature log in a neat fashion when called - Will also be used in the report
def tempLog_print():
    for i in range(len(tempLog)): #Separates the list of temps into a new line per value when calling the log
        tempV = tempLog[i]
###        timeV = timeLog[i]
        print(f"timeV {tempV}°C") #Stretch - Prints the timestamp and the temp value - To add the timestamp, change timeV to {timeV}

#Original attempt at printing the attendance report - The class_unit was printing <class : str> and I was unable to fix
#Keeping this commented out for tracking purposes
#def attendancePrint():
#    currentUnit = roomState.get("class_unit", "Unknown") #Attempts to pull the current unit, if there is none, sets to unknown
#    print(f"Lecturer: {lecturer} | Unit: {currentUnit}") #Prints who the lecturer is and what unit they are teaching
#    print("\nStudents: ")
#    for i in range(len(attendance)): #Prints student attendance - new line per student name
#        print(f"{attendance[i]}")
#    if len(attendance) == 0: #If no students are in the list
#          print("No students registered in this classrom.")

#Co-Pilots refinement - Outlined in Step 7
def attendancePrint():
    currentUnit = roomState.get("class_unit", "Unknown")
    # Check if the value is actually a string, not the str type itself
    if isinstance(currentUnit, type):
        currentUnit = "Unknown"
    print(f"Lecturer: {lecturer} | Unit: {currentUnit}")
    print("\nStudents:")
    if attendance:
        for student in attendance:
            print(student)
    else:
        print("No students registered in this classroom.")
        
#Checks the temperature - Denies access if outside of the defined range of between 16 and 28
def tempCheck():
    while True:
        temp = float(input("Current room temperature: "))
###        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") #Stretch to add a timestamp to the temp log
        tempLog.append(temp) #Adds the temperature to the tempLog
###        timeLog.append(timestamp) #Adds the date/time to the timelog
        if temp <16:
            print(f"The room temperature is below the threshold. Currently {temp:.1f}°C.")
            print(f"Room access has been denied. Only authorised personel may enter.")
            continue
        elif temp >28:
            print(f"The room temperature is above the threshold. Currently {temp:.1f}°C.")
            print(f"Room access has been denied. Only authorised personel may enter.")
            continue
        else:
            break

def roomCapacity(): #Checks against the current capacity - Denies entry if the room is at capacity
    global cardNumber
    while True:
        if roomState["capacity"] >=30: #If the room is at or above 30, deny access
            print("Access Denied. The room is at capacity.")
            break
        else: #Updates the attendance list and capacity
            studentName = studentCards[cardNumber]
            attendance.append(studentName) #Adds the student to the attendance register
            roomState["capacity"] += 1 #Increases capacity +1
            print(f"Welcome, {studentName}.")
            break
        
#Reads card access - different situations for different types of cards
def cardAccess():
    global cardNumber
    global lecturer
    while True:
        cardNumber = str(input("Please enter your card number. When finished, type 'Done': ")) #Would be connected to a card scanner
        if cardNumber in studentCards: #Checks for students
            roomCapacity()            
            continue
        if cardNumber in adminCards: #Checks for admins
            adminName = adminCards[cardNumber]
            print(f"Welcome, {adminName}.")
            continue
        elif cardNumber in teacherCards: #Checks for teachers
            teacherName = list(teacherCards[cardNumber].keys())[0] #Different from the other checks due to the unit being in a nested dict
            lecturer = teacherName
            roomState["class_unit"] = teacherCards[cardNumber][teacherName] #Sets the class_unit to the unit assigned to the teacher
            print(f"Welcome, {teacherName}. The unit has been set to {roomState['class_unit']}.")
            continue
        elif cardNumber == "Done" or cardNumber == "done": #continues to the next stage
            break
        else: #Error handling if the input is invalid
            print("Unauthorised user. If you think this is incorrect, please contact student services.")
            continue

def projectorStatus(): #Asks for and tracks the state of the projecter
    projector_state = str
    while True:
        projector_state = input("Is the projector working (Y)es or (N)o? ").strip().upper()#.strip().upper() - AI suggestion - Outlined in step 7
        if projector_state == "Y":
            roomState["projector_status"] = True #Sets the roomState dict state to True
            print(f"Projector status: {roomState['projector_status']}")
            break
        elif projector_state == "N":
            roomState["projector_status"] = False #Sets the roomState dict state to False
            print("IT has been alerted the projector is malfunctioning.")
            print(f"Projector status: {roomState['projector_status']}")
            break
        else:
            print("Please input a valid response. ")
            continue
            
def computerStatus(): #Same as projector status, just for the state of the computer
    computer_state = str
    while True:
        computer_state = input("Is the computer working (Y)es or (N)o? ").strip().upper() #.strip().upper() - AI suggestion - Outlined in step 7
        if computer_state == "Y":
            roomState["computer_status"] = True #Sets the roomStatedict state to True
            break
        elif computer_state == "N":
            roomState["computer_status"] = False #Sets the roomState dict state to false
            print("IT has been alerted the computer is malfunctioning.")
            break
        else:
            print("Please input a valid response. ")
            continue

def equipStatus_report(): #Prints the state of each device
    projector = roomState.get("projector_status", "Unknown") #Sets the state to unknown if not true or false - Avoids KeyError
    computer = roomState.get("computer_status", "Unknown") #Sets the state to unknown if not true or false - Avoids KeyError
    print(f"Projector: {projector} | Computer: {computer}")

def equipStatus(): #combines the Projector and Computer state functions together
    projectorStatus()
    computerStatus()
    equipStatus_report()  

def statusReport(): #Pulls together all reports - Attendance, temperature, equipment and combines them so they can be pulled in one go
    print("IT Equipment Status:")
    equipStatus_report()
    print("\nTemperature Log:")
    tempLog_print()
    print(" ")
    attendancePrint()
               

#Main menu options so that the user can select an option
def mainMenu():
    global userInput
    print("Options:\n1. Access \n2. Temperature\n3. Attendance\n4. Temperature log\n5. Equipment Status\n6. Status Report")

#Allows the user to return to the main menu after finishing up in a function
def runProgram():
    mainMenu()
    print("To call the menu at any time, input 'Menu'.")
    while True:
        choice = input("Please input a number to select a menu item: ") #Select menu item to activate function
        if choice == "1":
            cardAccess()
        elif choice == "2":
            tempCheck()
        elif choice == "3":
            attendancePrint()
        elif choice == "4":
            tempLog_print()
        elif choice == "5":
            equipStatus()
        elif choice == "6":
            statusReport()
        elif choice == "menu" or choice == "Menu":
            mainMenu()
        elif choice == "Quit": #Allows for checking dicts and lists for values - terminates code
            break
        else:
            print("Invalid option, please try again.")


runProgram() #Starts the run program function
