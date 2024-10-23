# ******************************************************
#                    15 - Oct - 2024
#                       Tuesday
# ******************************************************


# Tasks
# Ask the usetr to enter his/her name 
# name = input('Please Enter your name:- ')

#print Their name 
#print(name)


# Tasks
# Ask the uset to enter a rondom number
# Number = int(input('Please Enter a number:- '))
# print(Number)


# number = int("12")

# print(type(number))

# Std_Id = input ("Please Enter Your Id:- ")           # Ask the user to Enter his Id
# Std_Id2 = int(Std_Id)                                # Change the srting Id to integer 
# print(type(Std_Id2))  

# age = str(input("Geli Da'daada:- "))                  # Print the type of the new Id
# # Magac = str(age)
# print(type(age))


# age = input("Geli Da'daada:- ") 
# if not age.replace('.', '', 1).replace('-', '', 1).isdigit():
#     print(type(age))
# else:
#     print("Error: Please Enter a valid string.")












# # ******************************************************
print('******************************************************')
# Step 1: Ask the user to enter their Name
name = input("Please Enter Your Name:- ")


# Step 1: Ask the user to enter their ID
Std_Id = input("Please Enter Your Id:- ")

# Step 2: Use try-except to catch conversion errors
try:
     # Attempt to convert the input to an integer
     Std_Id2 = int(Std_Id)
     print(f"Hi {name}, welcome to the Somali National University")
     # Step 3: If successful, print the type
     print(f"Your Id is:- {Std_Id2}")
     print("Successfully Registred! ")
     # print(type(Std_Id2), end='\n')
     
except ValueError:
     # Handle the error if the input cannot be converted 
     print("Error: Please Enter a valid ID.")
