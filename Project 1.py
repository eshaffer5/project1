#!/usr/bin/env python
# coding: utf-8

# In[10]:


print("Welcome to the calculator")
print("Would you like to add, subtract, multiply, or divide?")
choice = input("Enter 'add' to add, 'multiply' to multiply, 'subtract' to subtract, or 'divide' to divide: ")
if choice == "add":
    addnum1 = input("Enter the first number you would like to add: ")
    addnum2 = input("Enter the second number you would like to add: ")
    addsolution = int(addnum1) + int(addnum2)
    print(str(addnum1) + " plus " + str(addnum2) + " equals " + str(addsolution))
elif choice == "subtract":
    subnum1 = input("Enter the first number you would like the second number to be subtracted from: ")
    subnum2 = input("Enter the second number you would like to subtract from the first number: ")
    subsolution = int(subnum1) - int(subnum2)
    print(str(subnum1) + " minus " + str(subnum2) + " equals " + str(subsolution))
elif choice == "multiply":
    multnum1 = input("Enter the first number you would like to multiply: ")
    multnum2 = input("Enter the second number you would like to multiply: ")
    multsolution = int(multnum1) * int(multnum2)
    print(str(multnum1) + " times " + str(multnum2) + " equals " + str(multsolution)) 
elif choice == "divide":
    divnum1 = input("Enter the first number you would like to divide by the second number, the dividend: ")
    divnum2 = input("Enter the second number you would like to divide the first number by, the divisor: ")
    divsolution = int(divnum1) / int(divnum2)
    print(str(divnum1) + " divided by " + str(divnum2) + " equals " + str(divsolution)) 
else:
    print("Sorry the input does not match a supported operation, please check your spelling and try again")


# In[ ]:




