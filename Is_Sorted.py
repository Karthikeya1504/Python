'''write a function called is_sorted that takes a list as a parameter
and returns True if the list is sorted in ascending order and False Otherwise


Sample input/output

1 2 3 6 5
False


6 7 8 9
True



'''


def is_sorted(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True        
arr_input = input()
arr1 = [int(x) for x in arr_input.split()]
print(is_sorted(arr1))
