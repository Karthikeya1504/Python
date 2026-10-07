'''Write a program to replace list’s item with new value if found.

NOTE : Replace only first occurance

Input Format:
-------------
Line 1: N space separated integers.
Line 2: integer, value to find
Line 3: integer, value to replace

input
Enter int values separated by space :33 45 65 23 67 33 45
Enter a number to find :45
Enter a number to replace :100

Output
[33, 100, 65, 23, 67, 33, 45]

Input:
Enter int values separated by space :12 24 54 12 24 35                                    
Enter a number to find :12                                                                
Enter a number to replace :19                                                             
Output:
[19, 24, 54, 12, 24, 35] 


'''


a=list(map(int,input("Enter int values separated by space :").split()))
n1=int(input("Enter a number to find :"))
n2=int(input("Enter a number to replace :"))
for i in range(len(a)):
    if a[i]==n1:
        a[i]=n2
        break

print (a)

