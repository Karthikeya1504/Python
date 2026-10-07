''' tuple subset
Check if a tuple is a subset of another tuple.

Sample Input: 
1 2 3 4 5 6 7 8 9
2 4 6

Sample Output:
True
'''

maintuple=tuple(map(int,input().split()))
subtuple=tuple(map(int,input().split()))
resulttuple=all(x in maintuple for x in subtuple)
print(resulttuple)
