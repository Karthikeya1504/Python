'''
It was the inaugural ceremony of "Fantasy Kingdom" Amusement Park and the park Management has announced some lucky prizes for the visitors on the first day. 
Based on this, the visitors whose ticket number has the last digit as 3 or 8, are declared as lucky winners and attracting prizes are awaiting to be presented for them.
Write a program to find if the last digit of the ticket number of visitors is 3 or 8.
Output should display as "Lucky Winner" if the last digit of the ticket number is 3 or 8.
Otherwise print "Not a Lucky Winner".

sample input 1:
123
sample output 1:
Lucky Winner

sample input 2:
1234
sample output 2:
Not a Lucky Winner
'''
a=int(input())
digit=0
while(a>0):
    digit=a%10
    if(digit==3 or digit==8):
       print ("Lucky Winner")
       break
    else:
       print("Not a Lucky Winner")
       break
