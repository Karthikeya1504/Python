mylist=["1","2","3","4","5","6","7","8","9","10"]

even_numbers=[int(num) for num in mylist if int(num)%2==0]
odd_numbers=[int(num) for num in mylist if int(num)%2!=0]

print("Even numbers: ",even_numbers)
print("Odd numbers: ",odd_numbers)
