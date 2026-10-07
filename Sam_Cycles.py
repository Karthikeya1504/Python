'''Sam cycles daily and data is captured on his smart watch.
At the end of the week, Sam would like to know the number 
of days,he has covered the EXACT distance.

Note:If the number of days is less than 7 and he has not covered
     the same distance print "-1"
     
     If number of days is equal to 7 and  he has not covered
     the same distance print "0"
     

Input Format:
---------------------------------
Line1: N space separated seven integers, daily Miles cycled for 1 week
Line2: Integer, Distance

Output Format:
--------------------------------------------
An integer value, Number of times he covered the exact distance

Sample Input-1:
----------------------------------
23 34 12 50 7 13 23
23

Sample Output-1:
----------------------------------
2

Sample Input-2:
--------------------------------------
12 5 6 30
15

Sample Output-2:
----------------------------------------
-1


Sample Input-3:
------------------------------------
18 16 19 15 19 13 11
8

Sample Output-3:
----------------------------
0

solution:'''


distances=list(map(int,input("daily Miles cycled for 1 week ").split()))
v=int(input())
l=len(distances)
count=0
if(l<7):
    print(-1)
else:
    for d in distances:
        if v==d:
            count+=1
    print(count)        
    
