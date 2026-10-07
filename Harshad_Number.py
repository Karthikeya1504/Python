'''
Write a program to check whether a number is a Harshad Number or not.
A harshad number in a given number base, 
is an integer that is divisible by the sum of its digits when written in that base.
Example: Number 200 is a Harshad Number because the sum of digits 2 and 0 and 0 is 2(2+0+0) and 200 is divisible by 2. 
Number 171 is a Harshad Number because the sum of digits 1 and 7 and 1 is 9(1+7+1) and 171 is divisible by 9.

Harshad Number is also called as Niven Number.

Enter a positive number :171                                                              
Harshad Number 


Enter a positive number :191                                                              
Not Harshad Number

'''

a=int(input("Enter a positive number :"))
sum=0
original=a
digit=0
while(a>0):
    digit=a%10
    sum=sum+digit
    a=a//10
if(original%sum==0):
    print("Harshad Number")
else:
    print("Not Harshad Number")
