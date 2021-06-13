Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("30 days 30 hours challenge")
30 days 30 hours challenge
>>> hours = "thirty"
>>> print("hours")
hours
>>> print(hours)
thirty
>>> days = "thirty days"
>>> print(days[0])
t
>>> print(days[0:5])
thirt
>>> challenge = "I will win"
>>> print(challenge[2:10])
will win
>>> print(challenge[7:10])
win
>>> print(len(challenge))
10
>>> challenge = "i will win"
>>> print(challenge.lower())
i will win
>>> print(challenge.upper())
I WILL WIN
>>> a = "30 days"
>>> b = "30 hours"
>>> c = a+b
>>> print(c)
30 days30 hours
>>> print(a+ " "+b)
30 days 30 hours
>>> test = "thirty days and thirty hours"
>>> x = text.casefold()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x = text.casefold()
NameError: name 'text' is not defined
>>> x = test.casefold()
>>> print(x)
thirty days and thirty hours
>>> x = test.capitalize()
>>> print(x)
Thirty days and thirty hours
>>> x = test.find()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x = test.find()
TypeError: find() takes at least 1 argument (0 given)
>>> x = test.find(x)
>>> print(x)
-1
>>> x  = test.isalpha()
>>> print(x)
False
>>> x = test.isalnum()
>>> print(x)
False
>>> 