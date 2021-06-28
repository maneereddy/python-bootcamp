#1) multplication using lambda function
a = lambda x,y:x*y
print(a(2,3))

#2)
from functools import reduce
fib = lambda n: reduce(lambda x , _:x+[x[-1]+x[-2]],range(n-2),[0,1])
print(fib(5))
#3)
nums =[1,4,3,5,6]
n = 2
filtered_numbers = list(map(lambda number : number*n,nums))
print(filtered_numbers)
#4)
list1 = [12,18,10,9,54]
m = 9
divisible_numbers= list(filter(lambda number:(number%m==0),list1))
print(divisible_numbers)
#5)
list2=[1,2,3,4,5,6,7]
evennumbers = list(filter(lambda number:(number%2==0),list2))
print(evennumbers)
