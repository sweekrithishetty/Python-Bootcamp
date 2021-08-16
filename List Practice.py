# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
# num_1 = int(input("Enter the number between 1-100 "))
# num_2 = int(input("Enter the number between 1-100"))
# while num_1 < 0 and num_2 < 0 or num_1 > 100 and num_2 > 100 or num_1 == num_2:
#     print("Please enter a valid number between 1- 100")
#     num_1 = int(input("Enter the number between 1-100 "))
#     num_2 = int(input("Enter the number between 1-100"))
# if num_1 < num_2:
#     for i in range(num_1,num_2+1):
#         print(i,end = ' ')
# else:
#     for i in range(num_2,num_1+1):
#         print(i,end = ' ')
    
'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
# user_input = input("Enter a string")
# # reverse = ''
# # for i in user_input :
# #     reverse = i + reverse
# # print(reverse)

# print(user_input[::-1])


'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
# user_input = int(input("Enter the number between 1-12 "))
# while user_input < 1  or user_input > 12:
#     print("Must be a user_input  ")
#     user_input = int(input("Enter the number between 1-12 "))
# print('==============')
# print()
# print(f'This is {user_input} times table')
# print()
# for i in range(1,13):
#     print(f'{i} * {user_input} ={user_input * i}')
    

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
# for i in range(1,13):
#     print('==============')
#     print()
#     print(f'This is {i} times table')
#     print()
#     for j in range(1,13):
#         print(f'{i} * {j} ={j * i}')

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
# user_input = input("Enter a squence of numbers")
# numbers = []
# while user_input.lower() != 'exit':
#     while not user_input.isdigit():
#         print("This is not valid")
#         user_input = input("Try again")
#     numbers.append(int(user_input))
#     user_input = input("Enter next number")
# print(sum(numbers/len(numbers)))
# total = 0
# for i in numbers:
#     total += i
# print(f'Mean is {total/len(numbers)} ')


'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
# n = 15
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)
    
'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
# n = 20
# a = 0
# b = 1
# fib_nums = []


# for i in range(n):
#     fib_nums.append(a)
#     a,b = b,a+b
# print(f'THe first {n} Fibonacci numbers are ,{fib_nums}')
'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''


star = '*'

for i in range(1,7):
    for j in range(1,6):
        if i == 1 and j < 6:
            print(star,end='')
        elif i == 2 and j == 1:
            print()
            print(star)
        elif i == 3 and j < 5:
            print(star,end='')
        elif i == 4 and j == 1:
            print()
            print(star)  
        elif i == 5 and j == 1:
            print(star)
        elif i == 6 and j == 1:
            print(star)  

'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
  

# # Numbers required
# n = 100

# # Instantiate empty lists
# evens = []
# odds = []

# for i in range(n+1):
#     if not i % 2:
#         evens.append(i)
#     else:
#         odds.append(i)
# print(f'The evens are {evens}')
# print(f'The odds are {odds}')        
        
    
    

    