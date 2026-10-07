'''Sorting Dictionary By Key

Before Sorting                                                                            
{5: 'abc', 1: 'xyz', 3: 'ram', 4: 'jak'}                                                  
After Sorting                                                                             
{1: 'xyz', 3: 'ram', 4: 'jak', 5: 'abc'}  
'''





d={5:'abc' , 1:'xyz' , 3:'ram' ,4:'jak'}
print("Before Sorting")
print(d)
myKeys=list(d.keys())
myKeys.sort()
sorted_dict={i:  d[i] for i in myKeys}
print("After Sorting")
print(sorted_dict)
