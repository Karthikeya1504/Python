'''Write a Python Program to Square Each Element of the List 
and Print List in Reverse Order

Input Format:
---------------------------------
N space separated integers, list of integers.

Output Format:
--------------------------------------------
N space seperated integers, resultant list.

Sample Input-1:
----------------------------------
1 2 3 4 5

Sample Output-1:
----------------------------------
[25, 16, 9, 4, 1]


Sample Input-2:
----------------------------------
-5 -4                                                                                                                   

Sample Output-2:
----------------------------------
[16, 25]

Solution:'''



a=list(map(int,input().split()))
n=len(a)
for i in range(n):
    a[i]=a[i]**2
a.reverse()
print(a)
