# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 08:43:59 2021

@author: SWEEKRITHI SHETTY
"""

'''
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''
# user = int(input("Enter the number between 1 and 5: "))
# if user == 1:
#     print('one')
# elif user == 2:
#     print('two')
# elif user == 3:
#     print('three')
# elif user == 4:
#     print('four')
# elif user == 5:
#     print('five')
# else:
#     print("Out of range")
    
'''
Question 2
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
'''
# user = input("Enter the string: ")
# user = user.lower()
# if user == 'one':
#     print('1')
# elif user == 'two':
#     print('2')
# elif user =='three':
#     print('3')
# elif user =='four':
#     print('4')
# elif user == 'five':
#     print('5')
# else:
#     print("Reject")

'''
Question 3
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
'''


# a = 3
# user = input('Guess the number: ')
# if user.isdigit():
#     user = int(user)
# if user == a:
#     print('The guess is correct')
# elif user < a:
#     print('Its too low')
# else:
#     print('It is too high')

'''
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
'''
# user  = input("Enter their name: ")
# a = len(user)
# if a > 5:
#     print('The total character\'s are:',a)
# else:
#     print("Length of your name is secret")

'''
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
'''
# num1 = int(input('Enter the number1:'))
# num2 = int(input('Enter the number2:'))
# if num1 >15 and num2 > 15:
#     print('Result :',num1*num2)
# elif num1 > 15 or num2 > 15:
#     print('Result4',num1+num2)
# else:
#     print('0')
    
'''
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
'''
num1 = int(input('Enter the number1:'))
num2 = int(input('Enter the number2:'))
num1,num2 = num2,num1
print('Swap variables are: ',num1,num2)
    

    