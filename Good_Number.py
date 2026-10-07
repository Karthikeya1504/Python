'''

write a program to check if a given number is good 
number or not A number is good if its every digit is
larger than the sum of digits which are on the right 
side of that digit. 

 For example 9620 is good number because 2 > 0, 6 > 2+0 
 and 9 > 6+2+0.  if the given number good number


Enter a number: 9620
Good number


Enter a number: 123                                                                       
Not good number
 
'''

a=int(input("Enter a number: "))
sum=0
k=1
digit=0
digit1=0
while(a>9):
    digit=a%10
    sum=sum+digit
    a=a//10
    digit1=a%10
    if(sum>=digit1):
        k=0
        break
    if(a<10):
        break
if(k==1):
    print("Good number")
else:
    print("Not good number")
