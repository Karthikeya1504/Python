'''Write a Python program which prints the count of integers and characters in 
   the given string

Hint :
You are allowed to use isnumeric(), isalpha() predefined string functions.

Input Format
---------------
Read a string

Output Format
---------------
Line1: Integer, Count of numbers
Line2: Integer, Count of letters

Sample Input:1
---------------
Hihoware123you4

Sample Output:1
---------------
4
11

Sample Input:2
---------------
22thFebruary2023

Sample Output:2
---------------
6
10

Solution:'''

a=input()
numbercount=0
lettercount=0
for char in a:
    if char.isnumeric():
        numbercount+=1
    elif char.isalpha():
        lettercount+=1    
print(numbercount)
print(lettercount)
