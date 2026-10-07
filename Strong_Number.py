'''
A number can be said as a strong number when the sum of the factorial of the 
individual digits is equal to the number.

For example, 145 is a strong number.
1 factorial + 4 factorial + 5 factorial == 145

i.e.
1 factorial  is 1
4 factorial  is 24
5 factorial  is 120
1+24+120 = 145  

Enter a number :145                                                                       
Number is a strong Number

Enter a number :120                                                                       
Number is not a strong Number
                                                                                                      
                 

'''




n=int(input("Enter a Number : "))
sum=0
temp=n
digit=1
while(n>0):
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if(sum==temp):
    print("{0} is Strong Number".format(temp))
else:
    print("{0} is not Strong Number".format(temp))
