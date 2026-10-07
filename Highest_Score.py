'''
John, a Math teacher conducts Maths test for a group of students. 
After the test he receives the marks list. 

Help John to find the higest score.

Input Format:
-------------
N space separated integers, marks of each student.

Output Format:
--------------
Print an integer, Highest score.

Sample Input-1:
---------------
10 54 30 75 43 65

Sample Output-1:
----------------
75

Sample Input-2:
---------------
60 60 60 60

Sample Output-2:
----------------
60
'''




numbers=list(map(int,input("marks of each student ").split()))
print(max(numbers))
