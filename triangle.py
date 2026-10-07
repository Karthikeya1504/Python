'''
Write a Python program to input three angles of a triangle.
  If a Triangle can be formed with given input, Check whether it forms a 
  ‘right Triangle’ or ‘Equilateral Triangle’ or ‘Normal Triangle’.
  If Triangle cannot be formed, display ‘Triangle cannot be formed’.

sample input:
90
90
90
sample output:
right Tringle

sample input:
60
60
90
sample output:
Triangle cannot be formed'''



a = int(input("Enter the first angle: "))
b = int(input("Enter the second angle: "))
c = int(input("Enter the third angle: "))
if(a+b+c== 180):
    if(a==60 and b==60 and c==60):
        print("Equilateral Triangle")        
    elif(a==90 or b==90 or c==90):
        print("Right Triangle")
    else:
        print("Normal Triangle")
else:
    print("Triangle cannot be formed")
