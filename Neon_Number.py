# A neon number is a number where the sum of digits of square of the number is equal to the number.”
'''
Enter a number :9                                                                         
9 number is  Neon number 

Enter a number :12                                                                        
12 number is  NOT Neon number


'''

a=int(input("Enter a number :"))
sum=0
square=0
digit=0
square=a*a
while square>0:
    digit=square%10
    sum=sum+digit
    square=square//10
if(sum==a):
    print("{0} number is  Neon number".format(a))
else:
    print("{0} number is  NOT Neon number".format(a))
