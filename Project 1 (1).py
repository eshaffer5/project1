#!/usr/bin/env python
# coding: utf-8

# In[15]:


print("Welcome to the calculator")
print("Would you like to add, subtract, multiply, or divide?")
print("Enter '1' to add, '2' to subtract, '3' to multipy, '4' to divide, '5' for exponentiation, or '6' to take a square root")
#Used numbers rather than words to simplify the process for the user
choice = input("Enter the number of the operation you would like the calculator to perform: ")

if choice == "1": 
    #Code for addition operator
    addnum1 = input("Enter the first number you would like to add: ")
    addnum2 = input("Enter the second number you would like to add: ")
    addsolution = int(addnum1) + int(addnum2)
    print(str(addnum1) + " plus " + str(addnum2) + " equals " + str(addsolution))
    #Added statements in the final print sequence to help the user understand what the program is doing
    
elif choice == "2":
    #Code for subtraction operator
    subnum1 = input("Enter the first number you would like the second number to be subtracted from: ")
    subnum2 = input("Enter the second number you would like to subtract from the first number: ")
    subsolution = int(subnum1) - int(subnum2)
    #Named all the vairables very similarly so that they would be easy to keep track of
    print(str(subnum1) + " minus " + str(subnum2) + " equals " + str(subsolution))
    
elif choice == "3":
    #Code for multiplication operator
    multnum1 = input("Enter the first number you would like to multiply: ")
    multnum2 = input("Enter the second number you would like to multiply: ")
    #Multiplication and addition proved to be more straightforward than division and subtraction, hence the better worded inputs
    multsolution = int(multnum1) * int(multnum2)
    print(str(multnum1) + " times " + str(multnum2) + " equals " + str(multsolution)) 
    
elif choice == "4":
    #Code for division operator
    divnum1 = input("Enter the first number you would like to divide by the second number, the dividend: ")
    divnum2 = input("Enter the second number you would like to divide the first number by, the divisor: ")
    divsolution = int(divnum1) / int(divnum2)
    print(str(divnum1) + " divided by " + str(divnum2) + " equals " + str(divsolution)) 
    
elif choice == "5":
    #Added exponentials as an additional operator
    expnum1 = input("Enter the first number you would like to be the base: ")
    expnum2 = input("Enter the second number you would like to be the power the base goes to: ")
    expsolution = int(expnum1) ** int(expnum2)
    print(str(expnum1) + " to the power of " + str(expnum2) + " equals " + str(expsolution)) 
    
elif choice == "6":
    #Added square roots as an even further operation
    import math #Had to use 'import math' to be able to utilize math.sqrt
    rootnum1 = input("Enter the number you would like to take the square root of: ")
    rootsolution = math.sqrt(int(rootnum1)) 
    #Wanted to add more root functionality but square root was the only one I could figure out
    print("The square root of " + str(rootnum1) + " is " + str(rootsolution))
    
else:
    print("Sorry the input does not match a supported operation, please check the number you input and try again")
#Added an else statement as a catch all in case someone mistyped a number or entered a number that isn't supported
#Most of my code is extremely straightforward which made adding comments difficult
#The variables and operators explains almost all of the code itself


# In[ ]:




