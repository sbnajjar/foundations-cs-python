
#################################  Assignment 2  #########################################
import os


def countDigits(number, iteration):
    
    remainder = number % (10**iteration)
    
    if remainder == number:
       return iteration
    else:
       iteration +=1
       return countDigits(number, iteration) 

def Choice1():

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

def Choice2():

    invalid_input = True
    while invalid_input:
        user_input = input("\nEnter a list of integers, separated by commas: ")
        user_list = user_input.split(",")
        global integer_list
        integer_list = []
        invalid_input = False
        for item in user_list:
            try:
                integer_list.append(int(item))
            except ValueError:
                print("Invalid input:", item, "is not an integer.")
                invalid_input = True

    
    global max_index
    max_index = len(integer_list)-1
    index=0
    max_number = integer_list[0]

    max_number = getMax(max_number,index)

    print("Maximum integer is: ", max_number)

    input("\nPress any Key to continue")

def main_Menu():

    choice = 0

    while choice != 4:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Count Digits")
        print("2. Find Max")
        print("3. Count Tags")
        print("4. Exit")
        print("- - - - - - - - - - - - - - -")
        choice = input("Enter a choice: ")
        
        if  choice == "1":
            Choice1()

        elif choice == "2":
            Choice2()

        elif choice == "3":
            print("you entered ", 3)
        elif choice == "4":
            print("you entered ", 4)
            break

main_Menu()



