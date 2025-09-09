#Stephen James | u3263912 | 09/09/2025 | Smart Classroom Monitor

#Allows for timers to be used for tracking, room bookings, etc
import datetime

roomState = {
    "projector_state" : bool,
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
teacherCards = { #Teacher card numbers
    "11111" : {"Julio Romero" : "Intro to IT - Lecture"},
    "11112" : {"Nipuni Wijesinghe" : "Intro to IT - Tutorial"},
    "11113" : {"Nishant Jagannath" : "Intro to Network Engineering - Lecture"},
    "11114" : {"Maddie Wong" : "Intro to Network Engineering - Tutorial"}
    }
attendance = [] #Attendance log

#Prints the temperature log in a neat fashion when called - Will also be used in the report
def tempLog_print():
    for i in range(len(timeLog)): #Separates the list of temps into a new line per value when calling the log
        tempV = tempLog[i]
        timeV = timeLog[i]
        print(f"{timeV} {tempV}°C") #Stretch - Prints the timestamp and the temp value

def attendancePrint():
    for i in range(len(attendance)):
        print(f"{attendance[i]}")



#Checks the temperature - Denies access if outside of the defined range of between 16 and 28
def tempCheck():
    while True:
        temp = int(input("Current room temperature: "))
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") #Stretch to add a timestamp to the temp log
        tempLog.append(temp)
        timeLog.append(timestamp)
        if temp <16:
            print(f"The room temperature is below the threshold. Currently {temp}°C.")
            print(f"Room access has been denied. Only authorised personel may enter.")
        elif temp >28:
            print(f"The room temperature is above the threshold. Currently {temp}°C.")
            print(f"Room access has been denied. Only authorised personel may enter.")
        else:
            break

def roomCapacity(): #Checks against the current capacity - Denies entry if the room is at capacity
    global cardNumber
    while True:
        if roomState["capacity"] >=30:
            print("Access Denied. The room is at capacity.")
            break
        else:
            studentName = studentCards[cardNumber]
            attendance.append(studentName)
            roomState["capacity"] += 1
            print(f"Welcome, {studentName}.")
            break
        

def cardAccess():
    global cardNumber
    while True:
        cardNumber = str(input("Please enter your card number: ")) #Would be connected to a card scanner
        if cardNumber in studentCards: #Checks for students
            roomCapacity()            
            continue
        if cardNumber in adminCards: #Checks for admins
            adminName = adminCards[cardNumber]
            print(f"Welcome {adminName}.")
            continue
        elif cardNumber in teacherCards: #Checks for teachers
            teacherName = list(teacherCards[cardNumber].keys())[0]
            roomState["class_unit"] = teacherCards[cardNumber][teacherName] #Sets the class_unit to the unit assigned to the teacher
            print(f"Welcome, {teacherName}. The unit has been set to {roomState['class_unit']}.")
            continue
        elif cardNumber == "Done": #continues to the next stage
            break
        else:
            print("Unauthorised user. If you think this is incorrect, please contact student services.")
            continue

#def equipStatus():
    

     



tempCheck()

cardAccess()

print(roomState)
print(attendance)
