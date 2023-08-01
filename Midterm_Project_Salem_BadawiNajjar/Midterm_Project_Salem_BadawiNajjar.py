"""
            Midterm Solution by SALEM BADAWI NAJJAR

Notes:

Given that data structure of ticketing system should include data in the following format:
tick101, ev003, fred, 20230802, 0
tick102, ev002, gio, 20230803, 2

and since ticket ID should be unique then the data structure used in the system is a dictionary with key & value as below:
- key :  ticket ID 
- value : list of the remaining relevant information  (event, user, date, priority)

The below is a default data dictionary to be exported initially to a newly created text file:

 default_data_dict = {
             "tick101": ["ev003","fred" ,"20230802" ,0], 
             "tick102": ["ev002","geo"  ,"20230801" ,0], 
             "tick103": ["ev001","salem","20230724" ,2],
             "tick104": ["ev003","karam","20230802" ,1],
             "tick105": ["ev001","geo"  ,"20230724" ,4],
             "tick106": ["ev001","salem","20230724" ,5]
            } 

The following constants are used as indexes in the Value list for each Key

EVENT    = 0
USER     = 1
DATE     = 2
PRIORITY = 3

Global dictionary "data_dict" holds the ticketing database after importing from external file

"""

import os                    # this will allow to use os.sysem function from os library
import datetime              # imorting datetime library


def clearScreen():

    os.system('cls' if os.name == 'nt' else 'clear') # to clear the output screen
    
    return
######################################################################################3

def importDataFile(input_file):

    default_data_dict = {
             "tick101": ["ev003","fred" ,"20230802" ,0], 
             "tick102": ["ev002","geo"  ,"20230801" ,0], 
             "tick103": ["ev001","salem","20230724" ,2],
             "tick104": ["ev003","karam","20230802" ,1],
             "tick105": ["ev001","geo"  ,"20230724" ,4],
             "tick106": ["ev001","salem","20230724" ,5]
            } 

    if not os.path.exists(input_file):  # check if data file exists in default directory
       
       #The data file does not exist. Therfore a new file will be added with default dictionary: default_data_dict
       
       exportDataFile(default_data_dict, "data.txt") 
       

    file = open(input_file)            # Opening the data file
    imported_data = file.readlines()   # Reading the data file content
    file.close()                       # Closing the data file

    imported_dict = dict()

    for line in imported_data:

        words = line.split(",")
        key = words[0].strip()
        
        value_list = list()
        value_list.append(words[1].strip())
        value_list.append(words[2].strip())
        value_list.append(words[3].strip())
        value_list.append(int(words[4].strip()))

        imported_dict[key] = value_list
  
    return imported_dict
    
###################################################################################  

def exportDataFile(data_dict, output_file):

    formatted_text = "" 

    for key, value in data_dict.items():

        formatted_text = (formatted_text + key +", " + value[0] +", " + value[1] + ", "
                         + value[2]+ ", "+ str(value[3]) +"\n")
    
    file = open(output_file,"w")     # open data file in write mode
    file.writelines(formatted_text)  # writing amended dict form to the output data file 
    file.close()                     # Closing the data file

    return
#####################################################################################

def displayStatistics():

    """
    Requirement: show event ID with highest tickets 

    STRATEGY:

    1) Prepare a dictionary with "eventID" as KEY &  "total ticket numbers" as VALUE for this event
    2) pick from this dictionary the highest VALUE which represents the highest number of tickets
    3) show to the user the highest number of tickets (VALUE) and show the associted event name (KEY)

    ex: { ev003 : 15 , ev001: 5 , ev002 :8 }

    The answer is ev003 which has 15 as total ticket numbers
    """

    events_dict = dict()

    for key, value, in data_dict.items():
        # get the event ID
        event_id = value[EVENT]     

        # check total no of tickets for this event, default is zero if not found
        no_tickets = events_dict.get(event_id, 0)   

        # increment the total no of tickets for this event by 1, store this value in the temp events dictionary
        events_dict[event_id] = no_tickets + 1      


    # get the event with maxium value, code refernce https://datagy.io/python-get-dictionary-key-with-max-value/
    event_with_max_tickets = max(events_dict, key=events_dict.get)

    # get the value for the subject event which represents the highest ticket numbers
    max_tickets = events_dict[event_with_max_tickets]

    # show the result

    
    clearScreen()

    print("The event with the highest number of tickets is:\n")

    print("Event: ", event_with_max_tickets)
    print("No of tickets: ", max_tickets)

    input("\nPress any Key to continue")
    return

###################################################################################

def getUsername():

    while True:
        username = input("\nEnter user name: ")
        if username =="":                                   # check if username is empty
            print("\nInvalid input. Username cannot be empty")
        elif username[0].isdigit():                         # check if username begins with digit
            print("\nInvalid input. Username must not begin with number") 
        else:
            username = "".join(username.split()).strip()   # remove inside and trainling spaces
            break
        
            
    return username    

###################################################################################

def getEventID():
    while True:
        try:
            value = int(input("Enter event No: "))
            if 0 <= value <= 999:
                break
            else:
                print("\nInvalid input. Please enter a positive three-digit numerical value.")
        except ValueError:
            print("\nInvalid input. Please enter a positive three-digit numerical value.")

    value = str(value)

    return "ev" + "0"*(3-len(value)) + value  # format event ID to correct form 

#######################################################################################3  
def getTicketID():
    while True:
        try:
            value = int(input("Enter Ticket No: "))
            if 0 <= value <= 999:
                break
            else:
                print("\nInvalid input. Please enter a positive three-digit numerical value.")
        except ValueError:
            print("\nInvalid input. Please enter a positive three-digit numerical value.")

    value = str(value)

    ticket_ID = "tick"  + "0"*(3-len(value)) + value  # format ticket ID to correct form 

    return ticket_ID

####################################################################################
def getEventDate():
    while True:
        try:
            day   = int(input("Enter day: "))
            month = int(input("Enter month: "))
            year  = int(input("Enter year: "))
            
            if (1 <= day <= 31) and (1 <= month <= 12) and (2010 <= year <= 2030) :
                break
            else:
                print("\nInvalid date.\n")
        except ValueError:
            print("\nInvalid date.\n")

    return  f"{year:04}" + f"{month:02}" + f"{day:02}"  # format date to proper datestamp YYYMMDD

###################################################################################

def newTickedID():

    highest_ticket_id = max(data_dict)

    highest_ticket_no = int(highest_ticket_id[4:7])

    new_ticket_no = highest_ticket_no + 1

    return "tick" + f"{new_ticket_no:03}"

###################################################################################

def getPriority():

    while True:
        try:
            value = int(input("Enter priority (0 to 9): "))
            if 0 <= value <= 9 :
                break
            else:
                print("\nInvalid input. Please enter a positive number from 0 to 9.")
        except ValueError:
            print("\nInvalid input. Please enter a positive number from 0 to 9.")

    return value


####################################################################################

def bookTicket(mode):

    """

        Requirement:  allow the admin to book a new ticket for an event by
                      specifying the username, event ID, date of the event and priority (the ticket ID
                      auto-incremented.

        STRATEGY:

        1) Clear the screen
        2) Get the username from the user and check validity (must not begin with a digit), and remove spaces
        3) Get the the eventID from the user by getting event integer number from 000 till 999 then convert
           it to string and add "ev" at the beginning. For instance, if the user enters 10 as event number 
           then the eventID would be "ev010" 
          
        4) Get the day, month, year of the event. After checking data validity,  derive eventDate using
           timestamp YYYYMMDD

        5) Derive the new Ticket ID by parsing the main data dictionary to get the highest TicketID and add the ID by 1
        6) Get priority from the user
        7) update the main data dictionary with a new key and new value representing the above new information.
   
     """ 
    
    clearScreen()

    if mode == "admin": 
        booking_username = getUsername() # input a username to be used for boking
        event_id    = getEventID()
        event_date  = getEventDate()
        priority    = getPriority()  
        ticket_id   = newTickedID()

    else:   # user mode
        booking_username = username      #  adopt the global username that was input during login
        event_id    = getEventID()
        event_date  = getEventDate()
        ticket_id   = newTickedID()
        priority    = 0                  #  default priority is zero in user mode 


    value_list = list()                    
    value_list.append(event_id)
    value_list.append(username)
    value_list.append(event_date)
    value_list.append(priority)


    data_dict[ticket_id] = value_list  # update main data dictionary with a new item representing the new booked ticket

    clearScreen()

    print("The following ticket was booked:\n")

    print("Ticket    Event     Date      Priority   Username" )      # display titles
    print("-------   -----     --------  --------   --------" )
    print(ticket_id," ", event_id ,"   ", event_date, "   ", priority,"     ", username )
      
    input("\nPress any Key to continue") 
    return
####################################################################################

""" Merge sort algorithm code reference: 
    https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/5_MergeSort/merge_sort_primitive.py
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(a,b):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)

    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    while i < len_a:
        sorted_list.append(a[i])
        i+=1

    while j < len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list


#######################################################################################3



def displayAllTickets():

    """
        Requirement:  show all tickets registered in the system, ordered by
                      event’s date and event ID (Today, Tomorrow, etc.). Old tickets should not be shown.

        STRATEGY:

        1) Get todays date from the system
        2) Parse the main data dictionary "data_dict" and build a new list "output_list" with elements 
           consisting of tickets with dates are todays date and beyond (tomorrow, after tomorrow, etc..).
           Each elementis a string containing eventDate, eventID, and ticketID

           For example if the main data dictionary contains the below information and todays date is equal to
             "20230801" ( 1st of August 2023)
            
           data_dict = {
                "tick101": ["ev003","fred" ,"20230802" ,0], 
                "tick045": ["ev002","geo"  ,"20230801" ,0], 
                "tick103": ["ev001","salem","20230724" ,2],
                "tick099": ["ev003","karam","20230802" ,1],
                "tick105": ["ev001","geo"  ,"20230724" ,4],
                "tick106": ["ev001","salem","20230724" ,5],
                "tick107": ["ev002","salem","20230801" ,5]
                         }

            Then the output list will contain the following:

            output_list = [
                            "20230802   ev003   tick101",
                            "20230801   ev002   tick045",
                            "20230802   ev003   tick099",
                            "20230801   ev002   tick107"  ]
            
            3) The output list is to be sorted using the merge sort algorithm which has the optimum speed
               and has the least average big O notation in comparison to other sorting techniques:

                a. Bubble Sort:    O(n^2)
                b. Selection Sort: O(n^2)
                c. Insertion Sort: O(n^2)
                d. Merge Sort:     O(nlogn)               

                Reference : https://chat.openai.com/share/ecc4c7fe-28c0-44b3-8714-89c9ed1c7341

              The sorted list will contain elements sorted by eventDate then by eventID then by ticketID
              In our example and after sorting, the output list will look like:

            output_list = [
                            "20230801   ev002   tick045",
                            "20230801   ev002   tick107",
                            "20230802   ev003   tick099",
                            "20230802   ev003   tick101"  ]
             
            4) Finally and in order to dispaly the final result, the following was done in order:
                    a. clear the screen
                    b. print the title string "Date       Event   Ticket"
                    c. loop the output string and print its elements line by line
                    
              As a result, the following will be dispalyed on the output console:

                            Date       Event   Ticket

                            20230801   ev002   tick045
                            20230801   ev002   tick107
                            20230802   ev003   tick099
                            20230802   ev003   tick101       
        """

    date_now = datetime.datetime.now() # getting today's date from the system


    # formatting today_date variable to datestamp "YYYYMMDD"
    today_date = f"{date_now.year:04}" + f"{date_now.month:02}" + f"{date_now.day:02}"  

    output_list = list()

    for key, value in data_dict.items():
        if value[DATE] >= today_date:
            # new_dict[key] = value
            event_date = value[DATE]
            event_id   = value[EVENT]
            ticket_id  = key
            line = output_list.append(event_date + "   " + event_id + "   " + ticket_id)

    output_list = merge_sort(output_list)  
    
    clearScreen()
    print("Date       Event   Ticket")    # display titles
    print("--------   -----   ------")
        
    for line in output_list :                 # dispaly tickets with event date today and onwards
        print(line)

    input("\nPress any Key to continue")  
    return
#########################################################################################
def changeTicketPriority():
    
    clearScreen()

    while True:
        ticket_ID = getTicketID()
        if not ticket_ID in data_dict:           # check if tickets exists in the database "main dictionary"
            print("Ticket does not match\n")
        else:
            break

    new_priority = getPriority()

    current_booking = data_dict[ticket_ID]

    current_booking[PRIORITY] = new_priority    # current booking list is modified by changing priority 

    data_dict[ticket_ID] = current_booking

    print("The ticket no", ticket_ID[4:7] ,"has the priority set to ",new_priority)

    input("\nPress any Key to continue")  

    return  

#########################################################################################
def disableTicket():

    clearScreen()

    while True:
        ticket_ID = getTicketID()
        if not ticket_ID in data_dict:           # check if tickets exists in the database "main dictionary"
            print("Ticket does not match\n")
        else:
            break

    del data_dict[ticket_ID]    

    print("The ticket no", ticket_ID[4:7] ," is now deleted")

    input("\nPress any Key to continue")  
    
    return

########################################################################################
def runEvents():
    """
        Requirement:  display today's events found in the list, sorted by priority,and remove them from the list.

        STRATEGY:

        1) Get todays date from the system

        2) Copy main data dictionary to a non-aliased copy called copied_data_dict

        3) Parse the copied_data_dict dictionary and build a new list called "output_list" with elements 
           consisting of tickets matching only today's date 

        4) delete tickets of todays date from main data dictionary  
         
        5) Sort the output list by priority using the optimum merge sort
                
        6) Finally and in order to dispaly the final result, the following was done in order:
                    a. clear the screen
                    b. print the titles
                    c. loop the output string and print its elements line by line

    """
 
    date_now = datetime.datetime.now() # getting today's date from the system

    # formatting today_date variable to datestamp "YYYYMMDD"
    today_date = f"{date_now.year:04}" + f"{date_now.month:02}" + f"{date_now.day:02}"  

    output_list = list()

    copied_data_dict =  dict(data_dict) # copying the main dictionary to another without aliasing

    for key, value in copied_data_dict.items():
        if value[DATE] == today_date:
            # new_dict[key] = value
            event_date = value[DATE]
            event_id   = value[EVENT]
            priority   = value[PRIORITY]
            ticket_id  = key
            line = output_list.append("    "+str(priority) + "      " + event_id + "   " + ticket_id)
            del data_dict[ticket_id]      # delete tickets of todays date from main data dictionary

    output_list = merge_sort(output_list)  
    
    clearScreen()

    print("Today's events :\n")

    print("Priority   Event   Ticket")    # display titles
    print("--------   -----   ------")
        
    for line in output_list :              # dispaly tickets with event date today and onwards
        print(line)

    input("\nPress any Key to continue") 
    return
#########################################################################################
def showAdminMenu():

    choice = 0

    while choice != 7:

        clearScreen()

        # display the menu

        print("1. Display Statistics")
        print("2. Book a Ticket")
        print("3. Display all Tickets")
        print("4. Change Ticket's Priority")
        print("5. Disable Ticket")
        print("6. Run Events")
        print("7. Exit")
        print("- - - - - - - - - - - - - - -")

        choice = input("Admin mode. Enter a choice: ")
        
        if  choice == "1":
           
            displayStatistics()
            
        elif choice == "2":
            
            bookTicket(mode="admin")

        elif choice == "3":

            displayAllTickets()

        elif choice == "4":
            
            changeTicketPriority()

        elif choice == "5":

            disableTicket()

        elif choice == "6":

            runEvents()

        elif choice == "7":
            break

    return    
##################################################################################

def showUserMenu():

    choice = 0

    while choice != 2:

        clearScreen()

        # display the user menu

        print("1. Book a Ticket")
        print("2. Exit")
        print("- - - - - - - - - - - - - - -")

        choice = input("User Mode. Enter a choice: ")
        
        if  choice == "1":
           
            bookTicket(mode="user")
            
        elif choice == "2":
            break

    return
##################################################################################



# defining constants to be used as indexes in the Value list for each Key

EVENT    = 0
USER     = 1
DATE     = 2
PRIORITY = 3

clearScreen()

attempt = 0

print("\nWelcome to Salem Ticketing System")

while attempt < 5 :

    print("\nProvide your username and password to login")
  
    username = getUsername()

    password = input("\nPassword: ") 

    data_dict = importDataFile("data.txt")      # Importing main data dictionary from external text file
    
    if password == "":
        showUserMenu()                          # Entering user mode
        exportDataFile(data_dict,"data.txt")   # Exporting main data dictionary to external text file
        break
    else:

        if username == "Admin" and password == "admin123123":
            showAdminMenu()                     # Entering admin mode
            break
        else:
            attempt +=1
            clearScreen()
            print("You still have", 5- attempt, "attempts to login as system admin")


clearScreen()

print("Thank you for using Salem Ticketing System\n")







