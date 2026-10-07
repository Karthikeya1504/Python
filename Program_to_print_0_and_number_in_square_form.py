'''
Write a program to print the following pattern

1 0 0 0 0
0 2 0 0 0
0 0 3 0 0
0 0 0 4 0
0 0 0 0 5
'''


a=int(input("Enter number of rows"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if(i==j):
            print(j,end=" ")
        else:
            print(0,end=" ")
    print()        
        
            
        
