
#################################  Assignment 3  #########################################
import os  # this will allow to use os.sysem function from os library
import json

def sumTuples(tup1,tup2):

    # Convert input strings to tuples
    

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



def exportJasonFile(orig_dict, output_file):

    formatted_dict = str(adjustDataForm(orig_dict))
    
      
    file = open(output_file,"w")   # open output file in write mode
    file.write(formatted_dict)     # writing amended dict form to the output file 
    file.close()                   # Closing the file

   
    input("\nPress any Key to continue")






def ImportJasonFile(input_file):

    file = open(input_file)       # Opening the file
    imported_data = file.read()   # Reading the file content
    file.close()                  # Closing the file

    imported_data = eval(imported_data) # convert string data to dict

    new_list = []

    
    for key, value in imported_data.items():
       temp_dict = {}
       temp_dict[key] = value
       new_list.append(temp_dict)
       
    print("find below the imported list of dictionaries:\n")
    print(new_list)


    input("\nPress any Key to continue") 
            

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

            print("Enter two tuples of the same length \n")

            input1 = input("\nEnter First Tupple: ")
            input2 = input("\nEnter Second Tupple: ")

            if len(input1) == len(input2): # compare both tuple lengths
               input1 = eval(input1)  # convert input1 string to tuple
               input2 = eval(input2) # convert input2 string to tuple
               sumTuples(input1,input2)
            else:
               print('\nBoth tuples must have the same length')
            
            input("\nPress any Key to continue") 
            

        elif choice == "2":
            
            # orig_dict contains nested dictionaries and lists, some dict kay values are: interger, str, boolean, and None

            orig_dict = {  5 : {1: { False : "fifty", None : [ 1, {100: "hundred"} ] }} , "3": [1,{10:"inside",20:"outside"}] , 4: "yes",  2: [1,2] }
            
            output_file = "c:\data\output_data.json"    # data folder c:\data
           
            exportJasonFile(orig_dict, output_file)

        elif choice == "3":

            input_file = "c:\data\data.json"

            ImportJasonFile(input_file)

        elif choice == "4":
            break


main_Menu()



