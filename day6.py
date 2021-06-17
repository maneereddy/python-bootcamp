capitals = {"maharastra":"mumbai"
            ,"AP":"amaravati"
            ,"telangana":"hyderabad"
            ,"tamilnadu":"chennai"}

capital = {"kerala":"thiruvananthapuram"
           ,"goa":"panaji"}
print("merging two dictionaries:",capitals.update(capital))

print(capitals)
#updating key value pair
capitals["tamilnadu"]="madras"
#removing element using pop function
print("removed element:",capitals.pop("AP"))
print("after removing the element using pop function:",capitals)
#removing element using popitem function
print("removed element:",capitals.popitem())
print("after removing element using popitem function:",capitals)

#two lists into dictionary
test_keys= ["ram","ravi","rahim"]
test_values=[1,2,3]
print("keys as :", str(test_keys))
print("values as:",  str(test_values) )
result = dict(zip(test_keys,test_values))
print(str(result))

#length of the set
numbers = {1,3,2,5}
print("length of the set:",len(numbers))

set1 = {1,3,2,5}
set2 = {11,22,33,55}
set3 = (set1.union(set2))
print("intersection of set1,set2 is:",set3)
print("removing set2 elements using for loop:")
set2={11,22,33,55}
for i in set2:
    set3.remove(i)
print("after removing ste2 from set3 we have elements of set1 are:",set3)


