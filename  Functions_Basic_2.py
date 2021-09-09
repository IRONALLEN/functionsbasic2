#  task 1
def countdown(num):
    for i in range (num,-1, -1):
        print(i)
countdown(5)

#task 2
count = [1,2]
def print_and_return(lis):
        print(lis[0])
        return lis[1]
print(print_and_return(count))

#task 3 
def first_plus_length(adder):
    for i in adder:
        print(adder[0] + len(adder))
        break
first_plus_length([3,4,5,6,7,8,9])
"""
#task 4
def values_greater_than_second(lis, lis_2):
    new_list = []
    item = lis
    i = lis_2
    print(item)
    for i in range(lis):
        if i > lis_2:
            print(i)
            
            
    if len(lis_2 ) < 2:
        print(False)

values_greater_than_second([5,1,2,6,2,7], [3])
"""
#this was my attemp not sure how to do it I would like some help 

#task 5 
#This Length, That Value 
def length_and_value(size, value):
    new_list = []
    for i in range(0, size, 1):
        new_list.append(value)
    return new_list
print(length_and_value(4,7))
print(length_and_value(6,2))