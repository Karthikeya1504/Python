'''Pattern
sample 1:
input = 5
output =
1                                                                                                                       
4 1                                                                                                                     
9 4 1                                                                                                                   
16 9 4 1                                                                                                                
25 16 9 4 1 

input = 3
output =
1
4 1
9 4 1
'''


a=int(input("input = "))
digit=0
for i in range(1,a+1):
    for j in range(i):
        print((i-j)**2,end=" ")
    print()    
