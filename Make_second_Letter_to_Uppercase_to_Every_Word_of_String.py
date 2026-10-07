'''Write a program to accept a string and display the string with
second alphabet of each word in upper case.


Input Format:
--------------------------------------
Read string

Output Format:
----------------------------------------
Print string with second alphabet upper case


Sample Input:
------------------------------------
apple banana                        

Sample Output:
----------------------------------------
aPple bAnana  

Solution:'''


a=input()
m=[]
for words in a.split():
    mx=words[:1] + words[1].upper() + words[2:]
    m.append(mx)
c_string=' '.join(m)
print(c_string)


