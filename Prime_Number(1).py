n=int(input("Enter a number :"))
k=n//2
i=2
c=0
if n<=2:
    print("Enter number Bigger than 1")
    exit()
while i<k:
    if n%i==0:
        c=1
        break
    i=i+1
if c==0:
    print("Given number is prime")
else:
    print("Given number is Not prime")
