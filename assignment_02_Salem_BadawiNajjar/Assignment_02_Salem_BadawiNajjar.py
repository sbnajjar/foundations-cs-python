
#################################  Assignment 2  #########################################
import os


def count_Digits(number, iteration):
    
    remainder = number % (10**iteration)
    
    if remainder == number:
       return iteration
    else:
       iteration +=1
       return count_Digits(number, iteration) 

def Choice1():

    
    number = int(input("\nEnter an integer : "))
      

    answer = count_Digits(number, iteration =1) 

    print("\nThe number of digits is: ", answer)
    
    input("\nPress any Key to continue")


def Choice2():

    number = int(input("\nEnter a list of integers to find the max : "))

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



