'''Write a program that takes two lists as input and 
returns True if the two lists share at least one element and False otherwise.

Input Format:
-------------
Line 1: N space separated integers.
Line 2: N space separated integers.

Output Format:
--------------
True or False

Sample Input-1:
---------------
1 2 3 4 5
5 6 7 8 9

Sample Output-1:
----------------
True

Sample Input-2:
---------------
1 2 3 4 5
6 7 8 9 10

Sample Output-2:
----------------
False
Solution:'''


a=list(map(int,input().split()))
b=list(map(int,input().split()))
n1=len(a)
n2=len(b)
x=False
for i in range(n1):
    if a[i] in b:
        x=True
        break
print(x)
