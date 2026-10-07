a=int(input("Enter a number :"))
fact=1
digit=0
sum=0
for i in range(1,a+1):
    fact=fact*i
print("The factorial of {0} is: {1}".format(a,fact))
n=fact
while(n>0):
    digit=n%10
    if(digit==0):
        sum=sum+1
    else:
        break
    n=n//10
print("{0}".format(sum))    
