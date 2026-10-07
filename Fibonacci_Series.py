'''
The Fibonacci numbers are the numbers in the following integer
sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
In mathematical terms, the sequence Fn of Fibonacci numbers is defined
by the recurrence relation.

 Fn = Fn-1 + Fn-2


with seed values :  F0 = 0 and F1 = 1.



Enter a number :5
1 2 3 5 8

'''

n=int(input("Enter a number: "))
a = 0
b = 1
if (n>0):
    print(a,end=" ")
for i in range(1,n+1):
    print(b, end=" ")    
    a, b = b, a + b
