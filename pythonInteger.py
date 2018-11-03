'''
This program reads in n integers and stores it in a list of integers.
The output of the program should display:
The list of integers
The average of the numbers in the list
The median value of the numbers
The number of even numbers in the list
'''
from statistics import mean, median

#ask user for times she/he wants to input value
user = int(input("How many integer do you want to input: "))

#use list comprehension to capture user input into a list
get_user = [int(input("Enter integer: ")) for i in range(user)]

print("The list of the integers is :", get_user)
print("The average of the numbers in the list is:",mean(get_user))
print("The median value of the numbers is:",median(get_user))

#use list comprehension to check for evem numbers
even_num = [j for j in get_user if j % 2 == 0]
print("The number of even numbers in the list is:", len(even_num))