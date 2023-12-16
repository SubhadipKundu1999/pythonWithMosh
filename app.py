
import math


# string in python
string1 = "Subhadip is a new developer"  # using double coute
print(string1)

string2 = 'this is a single couted string'  # using single coute
print(string2)


# how to define a multiline string ?

# --> using triple coute

str3 = '''
this 
is 
a
multi_line
string'''

print(str3)


# accessing specific charater in a string

name = "Subhadip"
print(name[0])  # assesing first character
print(name[-1])  # last character


# string is immutable
# name[0] = "w" TypeError: 'str' object does not support item assignment   ->


# string slicing
print(name[0:3])  # Sub || start from 0 to before 3 index

print(name[-4:-1])

print(name[3:])  # strating from index 3 to last index
print(name[:7])  # stat from 0 to index 6


# reverce a string

print(name[::-1])   # pidahbuS

print("". join(reversed(name)))  # pidahbuS


# perform updadtion im python string:

# python strings are not updateable
# step 1: coverting string to list
name_list = list(name)
print(name_list)  # ['S', 'u', 'b', 'h', 'a', 'd', 'i', 'p']

# update
name_list[3] = ""
print(name_list)  # ['S', 'u', 'b', '', 'a', 'd', 'i', 'p']

# convert pack to string
name = "".join(name_list)
print(name)  # Subadip


# Escape sequnces

# 1. print i'm subhadip
print("i\'m subhadip")

# 2 print I'm    subhadip
print("I\'m \t Subhadip")

# 3. print in a new line
print("this is line1\nthis is line 2")

# 4 ignoring escape sequence
print(r"i\'m subhadip\n kundu")  # i\'m subhadip\n kundu


# formating string
# Default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = f"{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String3 = "{l} {g} {f}".format(l='laddu', g='good', f='food')
print("\nPrint String in order of Keywords: ")
print(String3)


string5 = f"{0:b}".format(16)  # formating of integer
print(string5)  # binary value of 16 ->10000


# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)


# strings methods
s = "   ssssaass"
# print(s.count('s'))
# print(s.endswith('s'))
# print(s.find('a'))
# print(s.strip())
# print(s.isdecimal())
print(s.replace("s", "e",))


######################################################################################################################

# numbers
x = 1
print(x.bit_length())
x += 3
print(x)

x = 3+4j
print(type(x))  # <class 'complex'>

x = 3.67
print(type(x))  # <class 'float'>

print(round(x))  # 4
print(round(3.21))
j = 1+5j
k = 2+4j
l = j*k
print(l)


A = 2
print(float(A))

B = 5.6
print(int(B))

C = '3'
print(int(C))

D = 5
print(complex(D))

E = 6.5

print(complex(E))


# ###############type conversion
m = 4.5
n = 7.6
k = n+m
print(k)


# ############## math module ##########

print(math.sqrt(3))  # 1.7320508075688772
print(math.ceil(5.6))  # 6
print(math.floor(5.6))  # 5

# ways to choose k items from n items without repetition and without order.
k = 2
n = 4
print(math.comb(4, 2))


#

print(math.fabs(-4))  # 4.0
print(math.exp(10))    # 22026.465794806718
print(math.log10(10))  # 1.0
print(math.sin(60))  # -0.3048106211022167
print(math.degrees(math.pi))  # 180.0
