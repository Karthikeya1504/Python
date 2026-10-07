'''
Write program to find the sum and average of the list. 
The average of the list is defined as the sum of the elements divided by the number of elements.

Input Format:
-------------
N space separated integers.

Output Format:
--------------
Line 1: Print integer number, Sum of list elements
Line 2: Print float number, Average of list elements

Sample Input:
-------------
4 5 1 2 9 7 10 8

Sample Output:
--------------
46
5.75
'''


numbers = list(map(int, input().split()))
sum_of_elements = sum(numbers)
average_of_elements = sum_of_elements / len(numbers)
print(sum_of_elements)
print(f"{average_of_elements:.6f}")  
