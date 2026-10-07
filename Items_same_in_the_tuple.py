'''Check if all items in the tuple are the same
Input: 45 45 45 45
Expected output:
True
'''
a=tuple(map(int,input().split()))
result=True
for x in a:
    if x!=a[0]:
        result=False
        break
print(result)    
