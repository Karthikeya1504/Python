'''
Write program to input keys and values to a Dictionary and Print

Sample Input/Output:

Enter number of key in dictionery :3                                                      
Enter key :401                                                                            
Enter value :ram                                                                          
Enter key :402                                                                            
Enter value :jak                                                                          
Enter key :403                                                                              
Enter value :Mike                                                                         
{'401': 'ram', '402': 'jak', '403': 'Mike'}                                                 
401 : ram                                                                                 
402 : jak                                                                                 
403 : Mike


'''

d={}
n=int(input("Enter number of key in dictionery :"))
for i in range (n):
    key=input("Enter key :")
    value=input("Enter value :")
    d[key]=value
print(d)
for key,value in d.items():
    print(key,":",value)
