'''
common elements
Find the common elements between two tuples.

Example
input
1 2 3 4 5
4 5 6 7 8

output
(4,5)
'''
a=tuple(map(int,input().split()))
b=tuple(map(int,input().split()))
resulttuple=tuple(x for x in a if x in b)
print(resulttuple)
