"""
SUMMARY
data type transformations functions:
str()
int()
float()

data type
a=55
print(type(a))>> showing data type like 'int'

print("kübra","kösmene", sep="*")

print(*"python", sep="5")
p5y5t5h5o5n



"""
# father_name=input("your father name:")
# father_age=input("your fathers age:")
# your_name=input("your name:")
# print("Here is the {} and father name is {} and father age is {}".format(your_name,father_name,father_age))

# we can the procesess shortly like this

# father_name=input("your father name:")
# father_age=input("your fathers age:")
# your_name=input("your name:")
# print(f"Here is the {your_name} and father name is {father_name} and he is the age {father_age}")


# LIST TYPES
"""
Python lists are one of the most versatile data types that allow us to work with multiple elements at once
we putting inside list anywant data types thing 
list=[5, "heart", 87.59]

empty list
list=[]
"""
# list=[1,2,3,4,5,6,7,8,9,10]
# print(len(list))
# 10

# list=list("hello")
# print(list)
# ['h', 'e', 'l', 'l', 'o']


""" 
LIST INDEXING
indexing process do going to 0,1,2 counting list member

"""
# list=[0,1,2,3,4,5,6,78,9,856589]
# print(list[0])
# print(list[5])
# print(list[8])
# print(len(list))

# list[start:finis]
# print(list[4:8])
# print(list[::3])
# print(list[:: -1])

"""
METHODS OF LIST 

list=[1,2,3]
list2=[4,5,6]
list3= list + list2
list=[1,2,3,4,5,6]


list=[1,2,3]
print(list*3)
>> 1,2,3,1,2,3,1,2,3
print(list)
>>1,2,3
NOTE THAT!
list is not change its still has 3 member of its inside
if we change the list we opearted the a new list like that

list=list[]*3
print(list)
>> 1,2,3,1,2,3,1,2,3

NOTE THAT: CHANGE INSIDE MEMBER OF LIST
list=[1,2,3]
list[0]=5
print(list)
>> 5,2,3
"""

"""
APPEND METHOD
adding to list in a new data with .append() method
list2=["kösmene", "physics", 55, 99]
list2.append("ıstanbul")
print(list2)

POP METHOD
its the null proccesing is a removing to data en od the list
.pop(index number)


list2=["kösmene", "physics", 55, 99]
print(list2)
list2.append("ıstanbul")
print(list2)
print(list2.pop(2))
print(list2)


SORT METHOD
using the sort list elements in a number ıts qualifying to small toward biggest and in string qualifying to alphabetic rules
list=[4,6,8,9]
list.sort()
print(list.sort())

NESTED LIST
list1=[["apple", "orange"], [5,8], ["human", "animal"],[7000,895623147]]
print(list1)
print(list1[1][0])


"""

