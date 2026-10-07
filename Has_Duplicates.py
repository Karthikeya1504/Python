'''write a function called has_duplicates that takes a list 
and returns True if there is any element that appers more than once.
it should not modify the original list

1 2 3 4
False

9 9 5 5 8 8
True

'''


def is_duplicate(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                return True
    return False            
arr_input = input()
arr1 = [int(x) for x in arr_input.split()]
print(is_duplicate(arr1))
