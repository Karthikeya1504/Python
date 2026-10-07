'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:
a. All letters in this word are capitals, like "USA".
b. All letters in this word are not capitals, like "procareer".
c. Only the first letter in this word is capital, like "Google".
d. Otherwise, we define that this word doesn't use capitals in a right way. 

Input Format :
------------------------------
A string

Output Format :
------------------------------
Boolean value, True/False

Sample Input-1 :
------------------------------
USA

Sample Output-1 :
------------------------------
True  


Sample Input-2:
------------------------------
FlaG

Sample Output-2:
------------------------------
False


Sample Input-3:
------------------------------
Facebook

Sample Output-3:
------------------------------
True


Sample Input-4: 
------------------------------
losAnGeles

Sample Output-4: 
------------------------------
False
Solution:'''


a=input()
if a.isupper():
    print(True)
elif a.islower():
    print(True)
elif a[0].isupper() and a[1:].islower():
    print(True)
else:
    print(False)



