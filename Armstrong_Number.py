'''
An Armstrong Number is defined as the sum of cubes of the digit is equal to original number

Enter a Number : 153
It is Armstrong Number

'''

a=int(input("Enter a number"))
original=a
sum=0
digit=0
while a>0:
    digit=a%10
    sum=sum+digit*digit*digit
    a=a//10
if(original==sum):
    print("It is Armstrong number")
else:
    print("It is not a Armstrong number")
