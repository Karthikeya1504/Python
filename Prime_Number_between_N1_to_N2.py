
N1=int(input("Enter a number :"))
N2=int(input("Enter another number :"))
count=0
if((N2-N1)<=1):
    print(-1)
else:
    for j in range(N1,N2+1):
        if j>1:
            count=0
            for i in range(2,j+1):
                if(j%i==0):
                    count=count+1
                    break
                if count==0:
                    print("{0} is prime number".format(j))
                    break
        










