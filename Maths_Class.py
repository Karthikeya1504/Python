''' The students in maths class are given a problem to solve.
A number n is given,and the students have to perform following steps:
Add each digit of the number
Repeat this procedure until N becomes a single digitnumber.
your task is to help the students to perform the above steps and print the resultant digit number N.


input/output
Enter a number: 45                                                                        
The single-digit result is: 9

'''
N=int(input("Enter a number: "))
while N>=10:
    sum=0
    while N>0:
        sum=sum+N%10
        N=N//10
    N=sum
print("The single-digit result is: {0}".format(sum))
