"""

https://nbviewer.org/github/kosmenex/ basic connect of my book
https://nbviewer.org/github/mustafamuratcoskun/Sifirdan-Ileri-Seviyeye-Python-Programlama/tree/master/


"""
""""
DATA TYPES IN PYTHON
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

1) Numerical Data Type
 i. INTEGER:(int) integer is negative, positive number and including zero. integer domain[-∞,∞]
 ii. FLOAT: (float) floating point number, is a positive or negative whole number with a decimal point
 
 number=5
 float=55.98
 int=68.0 (python already that)

2) String Data Type:
 i) STRING:(str) defines all the characters on the keyboard, we must use the single quotes or double quotes
 
 name="kübra"
 print(name)
 name="kübra"

Division String Indexed:
name="kübra"
print(name[0],name[1],name[2],name[3],name[4])
>> k ü b r a
index:The function takes a set and sorts it from its first element. starts from 0
[starting index: end index: skip value ]
[0:5:-1]: start over, go up to index 8, don't take index 8, but read backwards


len(): function to find string character length
name="fahrettin cüreklibatur"
len(name)
print("len=",len(name))
>> len=22

name="kübra"
name[0]="c"
print(name)
giving a type error because we dont change inside string char. words
>>'str' object does not support item assignment

3) Boolean Data Type
 i) BOOL (bool): boolean data type has one of two possible values true and false
 logical transformations
 log= 5>8
 print(log)
>>> false
"""


int=55
float=25.5
print(int+float)
#>>80.5

number1=18
number2=59.89
type_transformations=type(number1)
print(type)
print(type(number2))
# two different way view of the what is the type of our data

"""
here we have functions that we have been using for notes,

print(): writing on terminal 
input(): giving a value from user
"""

# print()
print("Shall I compare thee to a summer’s day? Thou art more lovely and more temperate:")
# >>> Shall I compare thee to a summer’s day? Thou art more lovely and more temperate:

poetry="Shall I compare thee to a summer’s day?Thou art more lovely and more temperate:"
print(poetry)

"""
NOTE THAT: How do we make a stanza of our poem line? we use the escape sequence

Escape Sequence in Python:
\\	Backslash
\n	Newline
\r	Carriage Return
\t	Horizontal Tab
\b	Backspace
"""

print("Shall I compare thee to a summer’s day?\nThou art more lovely and more temperate:")

# sep() parameters

print("python","kübra","istanbul","physics")
# NOTE THAT: It puts a space between each statement in print by default
print("python","kübra","istanbul","physics" ,sep=" ")
# NOTE THAT: we see that already seperator parameters inside print functions so we dont see any difference apply to 2. examples

print("python","kübra","istanbul","physics" ,sep="")
# you see gaps between words are closed

# name=input("your name:")
# surname=input("your surname:")
# number=input("your id:")
# print(name, surname,id, sep="\n")

# end() parameters
person1="hello, how are you?"
person2="thanks, im fine and you"
print(person1, person2, sep="\n", end="?")

# NOTE THAT: an easier method for words
team="GALATASARAY"
print(*team, sep="❤")
# >>G❤A❤L❤A❤T❤A❤S❤A❤R❤A❤Y

# input() functions:function that retrieves data from user
# input()>> def input(__prompt: Any = ...) -> str
# Read a string from standard input. The trailing newline is stripped.


# Basic Math Operations
"""
1. + Addition
2. - Subtraction
3. * Multiplication
4. / Division
5. % Modulus Divides :left hand operand by right hand operand and returns remainder
6. ** Exponent
7. //	Floor Division: The division of operands where the result is the quotient in which the digits after the decimal 
 point are removed.
"""

number1=85
number2=98
name1="kübra"
surname="kösmene"
print(number1+number2)
print(name1+surname)
# print(number1+name1)

# Note That: !!TypeError: unsupported operand type(s) for +: 'int' and 'str'


# !!important difference
c1=c2=c3=c4=55
print(c1)
a1,a2,a3,a4=11,58,69,78
print(a1,a2,a3,a4)


# Python Program to Solve Quadratic Equation

"""
The standard form of a quadratic equation is:
ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0
The solutions of this quadratic equation is given by:

(-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
"""

# a=int(input("give a number="))
# b=int(input("give a number="))
# c=int(input("give a number="))
# d=(b**2)-(4*a*c)
#
# sol1=(-b-sqrt(d))/(2*a)
# sol2=(-b+sqrt(d))/(2*a)
# print(f"solution1={sol1} and solution2={sol2}")

