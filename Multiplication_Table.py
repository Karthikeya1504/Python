'''
Write a program to print Multiplication Tables

                                                                                  

'''




n=int(input("Enter a Number : "))
for i in range(1,n+1):
    for j in range(1,11):
        print("{0}*{1}={2}".format(i,j,i*j))
    print ()    
    
