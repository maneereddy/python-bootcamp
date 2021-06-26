#1)
print("Some Python errors are 1. Name error\n"
      "2. Type error\n"
      "3.Value error\n"
      "4.Index error\n"
      "5.Zero division error")
print("1.Name error")
age
print(age)
print("2. Type error")
a = "abc"+123
print(a)
print("3.value error")
int("123")
print("4.index number")
list = [1,2,3]
print(list[3])
print("5.zero division error")
a = 1
b= 0
print(a/b)
#2)calculator
num1 = int(input("enter a number"))
operator = input("enter a operator +,-,*,/")
num2 = int(input("enter a number"))

try:
    if operator =="+":
        print(num1+num2)
    elif operator =="-":
        print(num1-num2)
    elif operator =="*":
        print(num1*num2)
    elif operator =="/":
        print(num1/num2)
    else:
        print("something went wrong")
finally:
    print("the operation is completed")

#3)

try:
    one = 1
    if one==1:
        print(two)
        raise NameError("name error")
    if one>0:
        raise ValueError("value error")
except NameError as NE:
    print(NE)
except ValueError as VE:
    print(VE)


#4)
print("try-exception block is need "
      "to raise an exception to stop the execution,\n"
      "if there is no need to raise exception we don't use try-exception ")
#5)
try:
    x = int(input("enter a value"))
except:
    print("there is an error")
finally:
    print("operation completed")

