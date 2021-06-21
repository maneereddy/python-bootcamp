#1)
list1 = [1,2,3]
add = 2
for i in list1:
    print(i+add)
    i+=1

#2)pattern
n = int(input("enter number of rows:"))
for i in range(n):
    for j in range(n-i-1,-1,-1):
        print(j+1,end = " ")
    print()

#3)fibbonacci series
def fib(n):
    a = 0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
           c = a+b
           a = b
           b =c
           print(c)
n = int(input("enter a number"))
fib(n)

#4)
print("armstrong number: finding the length of the number and when total sum of power of each digit in the number equal to the number ,"
      "the it is called armstrong number")
i = int(input("enter a number"))
num = i
total = 0
n = len(str(i))
while(i!=0):
    digit = i%10
    total = total+digit**n
    i = i//10
if num==total:
    print("it's a armstrong number")
else:
    print("not a armstrong number")

#5)
n = 9
for i in range(1,11):
    print(n ,"x",i,"=",n*i )

#6)
m = int(input("enter a number"))
if m>0:
    print("positive number")
elif m==0:
    print("nunber equal to zero")
else:
    print("negative number")

#7)
d= int(input("enter the number of days:"))
y = int(d/365)
print(y,"year")

#8)
import math
x =90
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print(math.cosin(x))
print(math.sec(x))
print(math.cosec(x))
#9)
num1 = int(input("enter a number"))
operator = input("+,-,*,/")
num2 = int(input("enter a number"))
out = 0
if operator == "+":
    out = num1+num2
if operator =="-":
    out = num1-num2
if operator=="*":
    out = num1*num2
if operator =="/":
    out = num1/num2
print("answer is:",out)

