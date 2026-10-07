'''
Convert a tuple of strings to a single string.

input
I love programming
output
Iloveprogramming


'''
tup=tuple(input().split())
tup_res=''.join(tup)
print(tup_res)
