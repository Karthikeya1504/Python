'''
A Spy number is defined as the sum of the digits and product of the digits must be equal


Enter a Number : 1124
1124 is Spy Number

'''

a=int(input("Enter a Number"))
sum=0
product=1
digit=0
original=a
while(a>0):
    digit=a%10
    sum=sum+digit
    product=product*digit
    a=a//10
if(sum==product):
    print("{0} is Spy Number".format(original))
else:
    print("{0} is not Spy Number".format(original))
