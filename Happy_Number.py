'''
A Happy Number is defined as the sum of the squares of the digits until we get the sum as 1.
then that number is Happy Nummber


Enter a Number : 19
19 is Happy Number

Enter a Number : 13
13 is Happy Number

'''


n=int(input("Enter a Number : "))
sum=n
x=n
while(sum>9):
    sum=0
    while(x>0):
        d=x%10
        sum=sum+d*d
        x=x//10
    x=sum
if(sum==1):
    print("{0} is Happy Number".format(n))
else:
    print("{0} is not Happy Number".format(n))
