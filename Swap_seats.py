'''Harry and a group of 10 friends went for a movie and occupied continuous seats. 
Ron got a set at the end and near the AC vent. It was quite freezing there. 
He wanted to swap the seat with Harry who was seated at the beginning. 

Help Ron and Harry to swap there seats.

NOTE : Please use below input list in your coding

Input: ["Harry","Potter","David","Amelia","Noah","Liam","Charlene","Mike","Bruce","Ron"]
Expected Output: ["Ron","Potter","David","Amelia","Noah","Liam","Charlene","Mike","Bruce","Harry"]

'''


a=list(map(str,input().split()))
n=len(a)
a[0],a[n-1]=a[n-1],a[0]
print(a)

