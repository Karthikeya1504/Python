'''Write a function called sumEveryOther that takes 
in integers, 
and returns the sum of alternate numbers.

Sample input/output:

1 2 3 4 5 6 7 8 9                                                                         
25                                                                                        
20 

1 33 23 45 66 78                                                                         
100                                                                                       
156 




'''


def sumEveryOther(args):
    sum_result=0
    sum1_result=0
    index=0
    for arg in args:
        if index%2==0:
            sum_result += arg
        else:
            sum1_result += arg
        index += 1
    return sum_result,sum1_result    

user_input = input()
user_inputs = [int(x) for x in user_input.split()]
sum_result,sum1_result=sumEveryOther(user_inputs)
print(sum_result)
print(sum1_result)
