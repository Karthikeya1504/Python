'''
Write a program to print Multiplication Tables from 1 to 2

                                                                                  

'''




n=int(input("Enter a Number : "))
for i in range(1,n+1):
    for j in range(1,11):
        print("{0}*{1}={2}".format(i,j,i*j))
    print ()    
    
