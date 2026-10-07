'''Print the Sum of Key Value Pairs in a Given Dictionary
You need to create a list which has the sum of key-value pairs of a given dictionary. 
This can be done using a for loop and append() function. 

Given Dictionary                                                                          
{2: 8, 5: 20, 3: 15}                                                                      
Sum of Key-value pairs is = [10, 25, 18]



'''



d = {2:8,5:20,3:15}
print("Given Dictionary ")
print(d)
res_sumList=[]
for key in d:
    res_sumList.append(key+d[key])
print("Sum of Key-value pairs is = ",list(res_sumList))    
