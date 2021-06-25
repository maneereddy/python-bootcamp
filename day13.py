import re
#1)
string_value = "abAB12"
regex = re.compile(r"[^a-zA-Z0-9.]")
if regex.search(string_value):
    print("true")
else:
    print("false")

#2)finding the matching word with findall function

word = "abroad"
a = re.findall("ab",word)
print(a)

#3)
text = "one23"
x = re.compile(r".*[0-9]$")
if x.match(text):
    print("true")
else:
    print("false")
#4)
a = re.finditer(r"([0-9]{1,3}])", "print 2,11,3")
for i in a:
    print(i.group(0))
#5)
text2 = "Day 13 exercise"
b = "^[a-zA-Z0-9_]*$"
if re.search(b,text2):
    print("found")
else:
    print("not found")