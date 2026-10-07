# rotate the string
'''Print the following pattern
sample input
input =abcd
output =abcd
bcda
cdab
dabc


case=2
input=keshav
output=
Enter a string:                                                                     
keshav                                                                                    
eshavk                                                                                    
shavke                                                                                    
havkes                                                                                    
avkesh                                                                                    
vkesha
'''


a=input("Enter a String : ")
n=len(a)
for i in range(n):
    r = a[i:] + a[:i]
    print(r)
   
