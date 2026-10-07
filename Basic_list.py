'''
mylist=[14,25,86,36]
sum=0
for i in mylist:
    sum=sum+i
print(sum)
'''

'''
mylist=[14,25,86,36,14]
print(len(mylist))
'''

'''
mylist=[14,"raman",86.00,36,True]
print(mylist)
'''

'''
mylist=[14,25,86,36,40]
print(mylist[-1])
'''

'''
mylist=[14,25,86,36,40]
print(mylist[1:3])
'''

'''
mylist=[14,25,86,36,40]
print(mylist[:3])
'''

'''
mylist=[14,25,86,36,40]
print(mylist[2:])
'''

'''
mylist=[14,25,86,36,40]
mylist[2]=55
print(mylist)
'''

'''
mylist=[14,25,86,36,40]
mylist.insert(2,28)
print(mylist)
'''

'''
mylist=[14,25,86,36,40]
mylist.append(99)
print(mylist)
'''

'''
mylist1=[14,25,86,36,40]
mylist2=["Orange","Banana","Apple"]
mylist1.extend(mylist2)
print(mylist1)
'''

'''
mylist=[14,25,86,36,40]
mylist.remove(86)
print(mylist)
'''

'''
mylist=[14,25,86,36,40]
mylist.pop(1)
print(mylist)
'''

'''
mylist=[14,25,86,36,40]
mylist.clear()
print(mylist)
'''

'''
mylist=["Apple","Banana","Orange","Cherry"]
for x in mylist:
    print(x)
'''

'''
mylist=[]
for i in range(5):
    ele=input("Enter a element to append in list ")
    mylist.append(ele)
print(mylist)
'''

'''
mylist=list(("Apple","Banana","Cherry"))
for x in mylist:
    print(x)
'''

'''
thislist=["Apple","Banana","Cherry"]
i=0
while i<len(thislist):
    print(thislist)
    i=i+1
'''

'''
fruits=["apples","Banana","Cherry","Kiwi","Mango"]
newlist=[]
for x in fruits:
    if "a" in x:
       newlist.append(x)
print(newlist)        
'''

'''
fruits=["apples","Banana","Cherry","Kiwi","Mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)
'''


