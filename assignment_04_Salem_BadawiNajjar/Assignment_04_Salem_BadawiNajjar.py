
#################################  Assignment 3  #########################################
import os  # this will allow to use os.sysem function from os library

def clearScreen():

    os.system('cls' if os.name == 'nt' else 'clear') # to clear the output screen
    
    return

def getUsername():

    
    while True:
        username = input("\nEnter username: ")
        if username =="":                                   # check if username is empty
            print("\nInvalid input. Username cannot be empty")
        elif username[0].isdigit():                         # check if username begins with digit
            print("\nInvalid input. Username must not begin with number") 
        else:
            username = "".join(username.split()).strip()   # remove inside and trainling spaces
            break
        
            
    return username 

def addUser():

    username = ""
    while True:
       clearScreen()
       username = getUsername()
       if username in adjacency_list.keys():
          print("user:",username,"is already existing.\n")
       else:
           adjacency_list[username] = []
           print("user",username,"is now added\n")
           input("\nPress any Key to continue") 
           break   
    return         

def removeUser():

    clearScreen()
    username = getUsername()

    if username in adjacency_list.keys():

        del adjacency_list[username]              # remove user (vertex) from AL kets

        for key,value in adjacency_list.items():  # remove edge (connection) from all value lists of the AL
            if username in value:
                value.remove(username)
         
        print("user",username,"is now deleted with all relevant connectons\n")

    else:

      print("username",username,"does not exist.")      

    input("\nPress any Key to continue")
    return

def sendFriendRequest():

    clearScreen()
    print("\nUser 1 will be sending the friend request")
    user1 = getUsername()

    print("\nUser 2 will be receiving the friend request")
    user2 = getUsername()

    if  user1 == user2:                                             #both users are the same
        print("Usernames must be different. Please try again") 
        input("\nPress any Key to continue")
        return
    
    elif not (user1 in adjacency_list.keys()):                      # user1 is not registered in AL
        print("\nuser",user1,"is not recognized. Please try again") 
        input("\nPress any Key to continue") 
        return
    elif not (user2 in adjacency_list.keys()):                      # user2 is not registered in AL
        print("\nuser",user2,"is not recognized. Please try again") 
        input("\nPress any Key to continue") 
        return
    
    else:                                                           # both users are already registred in AL

        user1_friends = adjacency_list[user1]
        user2_friends = adjacency_list[user2]

        if not user2 in user1_friends:
            user1_friends.append(user2)
            adjacency_list[user1] = user1_friends
        
        if not user1 in user2_friends:
            user2_friends.append(user1)
            adjacency_list[user2] = user2_friends
            print("\nboth users", user1, "and", user2,"are now friends over the social media")
        else:
            print(user1, "and", user2,"are already connected")
        
        input("\nPress any Key to continue")

    return

def removeFriend():

    clearScreen()
    print("\nLogin with your username")
    user1 = getUsername()

    print("\nEnter the username of your friend ")
    user2 = getUsername()

    if  user1 == user2:                                             #both users are the same
        print("Usernames must be different. Please try again") 
        input("\nPress any Key to continue")
        return
    
    elif not (user1 in adjacency_list.keys()):                      # user1 is not registered in AL
        print("\nuser",user1,"is not recognized. Please try again") 
        input("\nPress any Key to continue") 
        return
    elif not (user2 in adjacency_list.keys()):                      # user2 is not registered in AL
        print("\nuser",user2,"is not recognized. Please try again") 
        input("\nPress any Key to continue") 
        return
    
    else:                                                           # both users are already registred in AL

        user1_friends = adjacency_list[user1]
        user2_friends = adjacency_list[user2]

        if not user2 in user1_friends:
            print("\nuser",user2,"is already not connected to",user1,". Please try again")
            return
        
        user1_friends = adjacency_list[user1]         # remove user2 from user1 friends
        user1_friends.remove(user2)
        adjacency_list[user1] = user1_friends

        user2_friends = adjacency_list[user2]         # remove user1 from user2 friends
        user2_friends.remove(user1)
        adjacency_list[user2] = user2_friends
                
        print(user1, "and", user2,"are now disconnected")
        
        input("\nPress any Key to continue")

    return

def listFriends():

    clearScreen()
    username = getUsername()

    if username in adjacency_list.keys(): 
        clearScreen()
        friends_list = adjacency_list[username]
        if len(friends_list) != 0:
            print(username, "friends's are:")
            print("-----------------------")
            for friend in friends_list:
                print(friend)
        else:     
            print(username,"has no connected friends.")   
    else:    
       print("user",username,"does not exist.")

    input("\nPress any Key to continue")
    return

def main_Menu():

    choice = 0

    while choice != 7:

        clearScreen()

        # display the menu

        print("1. Add a user to the platform")
        print("2. Remove a user from the platform")
        print("3. Send a friend request to another user")
        print("4. Remove a friend from your list")
        print("5. View your list of friends")
        print("6. View the list of users on the platform")
        print("7. Exit")
        print("- - - - - - - - - - - - - - -")

        choice = input("Enter a choice: ")
        
        if  choice == "1":
          
            addUser()           

        elif choice == "2":
            
            removeUser()

           
        elif choice == "3":

           sendFriendRequest()

        elif choice == "4":

           removeFriend()  

        elif choice == "5":

           listFriends()

        elif choice == "6":

           clearScreen()
           print("Users List")
           print("----------")
           for key in adjacency_list.keys(): 
               print(key) 

           input("\nPress any Key to continue") 
           
        elif choice == "7":
            clearScreen()
            print("Thank you for using Social Media Platform\n")
            break

global adjacency_list 

adjacency_list = dict()

main_Menu()



