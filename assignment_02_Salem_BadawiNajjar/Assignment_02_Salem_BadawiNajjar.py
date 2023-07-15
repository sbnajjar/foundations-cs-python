
#################################  Assignment 2  #########################################
import os  # this will allow to use os.sysem function from os library


def countDigits(number, iteration):
    
    remainder = number % (10**iteration)
    
    if remainder == number:
       return iteration
    else:
       iteration +=1
       return countDigits(number, iteration) 

def choice1():

    while True:
        number = input("Enter an integer : ")
        try:
            number = int(number)
            break
        except ValueError:
            print("")

    answer = countDigits(number, iteration =1) 

    print("\nThe number of digits is: ", answer)
    
    input("\nPress any Key to continue")


def getMax(max_number,index):

    if max_number < integer_list[index]:

        max_number = integer_list[index]

    if index < max_index:
       return getMax(max_number,index+1)
    else:
       return max_number

def choice2():

    invalid_input = True
    while invalid_input:
        user_input = input("\nEnter a list of integers inside brackets and separated by commas: ")
        
        user_input = str(user_input)

        if user_input == "[]":
           print("Maximum integer is: ", 0)
           input("\nPress any Key to continue")
           return
        

        user_input = user_input[1:]                  # remove left bracket from user input
        user_input = user_input[:len(user_input)-1]  # remove right bracket from user input

        user_list = user_input.split(",")

        global integer_list
        integer_list = []
        invalid_input = False
        for item in user_list:
            try:
                integer_list.append(int(item))
            except ValueError:
                invalid_input = True

          
    global max_index
    max_index = len(integer_list)-1
   
    index=0
    max_number = integer_list[0]

    max_number = getMax(max_number,index)

    print("Maximum integer is: ", max_number)

    input("\nPress any Key to continue")

def matchCount(tag, index, occurence):

    try: 
        if code_string.index(tag,index) > 0:
            if index < len(code_string):
                occurence =  matchCount(tag, index+1, occurence + 1)
        else: 
            return 0
        
    except ValueError:  
        return occurence
    
       
    return occurence

def choice3():

    ### Alternative way to get input from external file ####
   
    #code_file = 'code.txt'  
    #file = open('./' + code_file)  # Opening the file
    #code_string = file.read()   # Reading the file content
    #file.close()            # Closing the file

    global code_string

    code_string = """<html>
                <head>
                <title>My Website</title>
                </head>
                <body>
                <h1>Welcome to my website!</h1>
                <p>Here you'll find information about me and my hobbies.</p>
                <h2>Hobbies</h2>
                <ul>
                <li>Playing guitar</li>
                <li>Reading books</li>
                <li>Traveling</li>
                <li>Writing cool h1 tags</li>
                </ul>
                </body>
                </html> """
    
    tag = input("Specify tag to count its occurences:")
    tag ="<"+tag+">"

    
    code_string = "<li> <li>"
    
    index = 0
    occurence = 0

    try:
        tag_count= matchCount(tag,index,occurence)
                
    except ValueError:
        print("out of range")

    print("the number of occurences is", tag_count)  

    input("\nPress any Key to continue") 
    

    return

def main_Menu():

    choice = 0

    while choice != 4:

        os.system('cls' if os.name == 'nt' else 'clear') # to clear the output screen
        print("1. Count Digits")
        print("2. Find Max")
        print("3. Count Tags")
        print("4. Exit")
        print("- - - - - - - - - - - - - - -")
        choice = input("Enter a choice: ")
        
        if  choice == "1":
            choice1()

        elif choice == "2":
            choice2()

        elif choice == "3":
            choice3()

        elif choice == "4":
            break

main_Menu()



