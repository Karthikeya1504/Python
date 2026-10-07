a=int(input("Enter a number :"))
prime=True
if a<2:
    print=False
else:
    for i in range(2,a):
        if a%i==0:
            prime=False
            break
if prime:
    print("Given number is Prime ")
else:
    print("Given number is Not prime")
