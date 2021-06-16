numbers = []
#adding elements using INSERT,APPEND, EXTEND functions
numbers.append(1)
print("list after appending element:",numbers)
numbers.insert(1,2)
print("list after inserting element:",numbers)
list2=[3,4,5]
numbers.extend(list2)
print("list after extending:",numbers)
#deleting elements using POP,REMOVE,DEL functions
print(numbers)
numbers.pop(3)
print("print list after poping:",numbers)
numbers.remove(5)
print("print list after removing:",numbers)
del numbers[0:]
print("print list after deleting: ",numbers)
#finding minimum,maximum values using functions
values = [2,3,6,1,4]
minimun_value = min(values)
print("minimum value is",minimun_value)
maximum_value = max(values)
print("maximum value is",maximum_value)

#2)reversing tuple

def reverse(nums):
    new_tup = ()
    for i in reversed(nums):
        new_tup = new_tup+ (i,)
    print(new_tup)
nums = (1,2,3,4)
reverse(nums)

#3) question
#converting tuple to list
values = (2,3,4,5)

alist = list(values)

print(alist)


