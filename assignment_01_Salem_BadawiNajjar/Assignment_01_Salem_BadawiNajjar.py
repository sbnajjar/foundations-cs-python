
#################################  Module 1 : Calculate Factorial #########################################

def getFactorial(num):
    
    num = int(num)
    while num < 0 :
      print("Negative number is not acceptable. ")
      num = int(input("Enter positif number to calcute its factorial: "))
      
    answer = 1  
    for i in range(num):
      i += 1
      answer = answer * i
          
    return answer
###########################################################################################################


#################################  Module 2 : List of divisors ############################################

def listDivisors(num):

    num = int(num)
    answer = []

    for i in range(num):
      i += 1
      if (num % i) == 0:
        answer.append(i)

    return answer


###########################################################################################################


#################################  Module 3 : Reverse string ##############################################

def reverseString(user_input):
    
    input_string = str(user_input)    #  Validate input

    span = len(input_string)
    
    answer = ""

    for i in range(span):
      answer = answer + input_string[span-i-1]

    return answer


#################################  Module 4 : List of even numbers ########################################

def evenNumbers(user_input):
   
    user_input = str(user_input)
    user_input = user_input[1:]                  # remove left bracket from user input
    user_input = user_input[:len(user_input)-1]  # remove right bracket from user input

    list_of_numbers = user_input.split(",")      # fill the given numbers in a new list

    answer = []

    for i in list_of_numbers:

      if (int(i) % 2) == 0:
        answer.append(int(i))

    return answer
    
#################################  Module 5 : Check Strong Password  #######################################

def checkPassword(user_password):
    
    strong_password = False

    valid_length = False

    contains_lower_case = False

    contains_upper_case = False

    contains_special_char = False

    contains_digit = False

    if len(user_password) >= 8 :
       valid_length = True

    for i in user_password:
      if i.isupper():
         contains_upper_case = True
      elif i.islower():
         contains_lower_case = True
      elif i=="#" or i== "?" or i== "!" or i == "$":
         contains_special_char = True
      elif i.isdigit():
         contains_digit = True

    if contains_lower_case and contains_upper_case and contains_special_char and contains_digit and valid_length:
      strong_password = True

    if strong_password:
      print("Strong password")
    else:
      print("Weak password")  


#################################  Testing all modules ####################################################


# Testing Module 1
num = input("Enter positif number to calcute its factorial: ")
print(getFactorial(num))


# Testing Module 2
num = input("Enter an number to list its divisors: ")
print(listDivisors(num))


# Testing Module 3
user_input = input("Enter a string to reverse: ")
print(reverseString(user_input))

# Testing Module 4
user_input = input("Enter a list of numbers between two brackets. For example [1,4,13]: ")
print(evenNumbers(user_input))

# Testing Module 5
user_input = input("Enter your password: ")
checkPassword(user_input)

