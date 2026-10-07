a=int(input("Enter the integer number:"))
reverse=0
while a!=0:
    reverse=reverse*10+(a%10)
    a=a//10
print("The reverse numberis:{0}".format(reverse))    
