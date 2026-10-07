'''
capitalize the first letter of each word  and then reconstruct the string 
with the capitalized words using for loop.

case=1
input=keshav memorial college of engg
output=
Enter a String :                                           
Keshav Memorial College Of Engg



case=2
input=WELCOME TO PYTHON CLASS
output=
Enter a String :                                                   
Welcome To Python Class 



'''

a=input("Enter a String :")
words=[]
for word in a.split():
    words.append(word.capitalize())
c_string=' '.join(words)
print(c_string)

