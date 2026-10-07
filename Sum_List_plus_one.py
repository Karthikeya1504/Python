#program to take input,sum of the elements,add 1 to the sum and create a new list of digits

numbers=list(map(int,input("Enter a number ").split()))
print(numbers)
total=sum(numbers)+1
#constructing a new list with the sum as its individual digits
new_list={int(digit)for digit in str(total)}
print(f"New list of digits from the sum is: {new_list}")
