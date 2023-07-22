
#################################  Assignment 3  #########################################
import os  # this will allow to use os.sysem function from os library
import json

def choice1():

    input1 = input("\nEnter First Tupple: ")
        
    input2 = input("\nEnter Second Tupple: ")

    # Convert input strings to tuples
    tup1 = eval(input1)
    tup2 = eval(input2)

    sum_tup = ""

    for i in range(len(tup1)):
        sum = int(tup1[i]) + int(tup2[i])
        sum_tup = sum_tup + str(sum)
        if i != len(tup1)-1:
           sum_tup =  sum_tup + ","
    
    sum_tup = eval(sum_tup)
    print("\nThe sum of both tuples is:", sum_tup)

    input("\nPress any Key to continue")

def adjustDataForm(data_form):

    
    if isinstance(data_form, dict):
        adjusted_value = {}
        for key,value in data_form.items():
        
            adjusted_key = str(key) 

            if isinstance(value, dict) or isinstance(value, list):  # if the dict value is a nested dict or list
               new_value = adjustDataForm(value)                    # calling adjustDataForm recursively
               

            else:                                                   # value is not dict or list, it can be text
               new_value = value   
               

            if isinstance(key, bool):
               adjusted_key = adjusted_key.lower() 

            elif key is None:
               adjusted_key  = "null"

            adjusted_value[adjusted_key] = new_value

    elif isinstance(data_form, list):
        
        for i in range(len(data_form)):

            data_form[i] = adjustDataForm(data_form[i])

        adjusted_value = data_form
    else:
        adjusted_value = data_form  

    return adjusted_value



def writeJasonFile(orig_dict, output_file):

    formatted_dict = str(adjustDataForm(orig_dict))
    
      
    file = open(output_file,"w")   # open output file in write mode
    file.write(formatted_dict)     # writing amended dict form to the output file 
    file.close()                   # Closing the file

   
    input("\nPress any Key to continue")






def choice3():
    input("\nPress any Key to continue") 
    ### Alternative way to get input from external file ####
"""
    code_file = 
    file = open(code_file)  # Opening the file
    code_string = file.read()   # Reading the file content
    file.close()            # Closing the file

    #print(code_string)

    write_data = str({"2": "123", "false": [1, 2], "1": [1, 3]})

    #write_data = "{\n" + str('"2": "123"') + str(",\n")  + str('"false": [1, 2], "1": [1, 3]}')


    print(write_data)
"""

        

def main_Menu():

    choice = 0

    while choice != 4:

        os.system('cls' if os.name == 'nt' else 'clear') # to clear the output screen

        # display the menu

        print("1. Sum Tuples")
        print("2. Export JSON")
        print("3. Import JSON")
        print("4. Exit")
        print("- - - - - - - - - - - - - - -")

        choice = input("Enter a choice: ")
        
        if  choice == "1":
            choice1()

        elif choice == "2":
            
            # orig_dict contains nested dictionaries and lists, some dict kay values are: interger, str, boolean, and None

            orig_dict = {  5 : {1: { False : "fifty", None : [ 1, {100: "hundred"} ] }} , "3": [1,{10:"inside",20:"outside"}] , 4: "yes",  2: [1,2] }
            
            output_file = "c:\data\output_data.json"    # data folder c:\data
           
            writeJasonFile(orig_dict, output_file)

        elif choice == "3":
            choice3()

        elif choice == "4":
            break


main_Menu()



