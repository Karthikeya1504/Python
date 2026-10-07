'''
Write a program to remove all occurrences of a specific item from a list.

Input Format:
-------------
Line 1: N space separated integers.
Line 2: integer, value to remove

Output Format:
--------------
Resultant list.

Sample Input-1:
---------------
5 20 15 20 25 50 20
20

Sample Output-1:
----------------
[5, 15, 25, 50]

Sample Input-2:
---------------
5 20 15 20 25 50 20
200

Sample Output-2:
----------------
[5, 20, 15, 20, 25, 50, 20]


'''
numbers=list(map(int,input().split()))
value_to_remove=int(input())
result=[num for num in numbers if num !=value_to_remove]
print(result)
