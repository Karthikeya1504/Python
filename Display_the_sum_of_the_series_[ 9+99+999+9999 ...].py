
'''Display the sum of the series [ 9 + 99 + 999 + 9999 ...]


Input the number or terms :5
9
99
999
9999
99999
The sum of the series : 111105


Input the number or terms :3
9
99
999
The sum of the series : 1107
'''


n=int(input("Input the number or terms :"))
sum=0
num=9
for i in range(n):
    print(num)
    sum=sum+num
    num=num*10+9
print("The sum of the series : {0}".format(sum))    
