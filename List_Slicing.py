'''Write a Python Program to split a list in half 
and store the elements in two different lists.

Input Format:
-------------
N space separated integers, list of integers.

Output Format:
--------------
Line 1 : Print List of integers, first half of input list.
Line 2 : Print List of integers, second half of input list.


case=1
input=37 14 21 87 82 75 15 46 73 22
output=
First half: [37, 14, 21, 87, 82]                                                          
Second half: [75, 15, 46, 73, 22]

case=2
input=81 65
output=
First half: [81]                                                                          
Second half: [65]

case=3
input=10 45 63 78 99
output=
First half: [10, 45]                                                                      
Second half: [63, 78, 99] '''


input_list = list(map(int,input().split()))
midpoint = len(input_list)//2
first_half = input_list[:midpoint]
second_half = input_list[midpoint:]
print("first half : ",first_half)
print("second half : ",second_half)
