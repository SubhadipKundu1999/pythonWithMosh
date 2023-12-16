# if/else
temp = 30

if temp > 40:
    print("it is warm")
elif temp > 20:
    print("it is normal")
else:
    print("it is cool")

# ternary
age = 20
message = "\neligible" if age >= 18 else "Not eligible"
print(message)


# Logical
student = True
if not student:
    print("not elibible")
else:
    print("Eligible")

high_income = False

if (not student or high_income) and age > 20:
    print("eligible")

else:
    print("not elibible")


# short circuit evalution

# evalution stop as soon as an condition false in case of and operator
# evalution stop as soon as an condition is true in case of or oprtator


# Q

    print(10 == '10')
    if 10 == '10':
        print("a")
    elif "bag" > "apple" and "bag" > "cat":
        print("b")
    else:
        print("c")


# for loop

for number in range(3):  # starting from 0 to 3
    print("Attempt", number+1, (number+1) * ".")

# output:
# Attempt 1 .
# Attempt 2 ..
# Attempt 3 ...


for number in range(3, 5):  # starting from 3 to before 5
    print("Attempt", number+1, (number+1) * ".")
# o/p
# Attempt 1 .
# Attempt 2 ..
# Attempt 3 ...
# Attempt 4 ....
# Attempt 5 .....

for number in range(2, 10):  # starting from  to before 10 ie upto 9
    print("Attempt", number, (number) * ".")
# o/p
# Attempt 2 ..
# Attempt 3 ...
# Attempt 4 ....
# Attempt 5 .....
# Attempt 6 ......
# Attempt 7 .......
# Attempt 8 ........
# Attempt 9 .........

# starting from  to before 10 ie upto 9 and at a time go 2 step
for number in range(2, 10, 2):
    print("Attempt", number, (number) * ".")
# o/p
# Attempt 2 ..
# Attempt 4 ....
# Attempt 6 ......
# Attempt 8 ........


# for... else

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("attempted 3 time and failed")

# 0/p
    # Attempt
    # Successful


successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("attempted 3 time and failed")

# 0/p
# Attempt
# Attempt
# Attempt
# attempted 3 time and failed


# nested loop

for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")
# o/p
# (0, 0)
# (0, 1)
# (1, 0)
# (1, 1)
# (2, 0)
# (2, 1)


# range object
print(type(5))         # <class 'int'>
print(type(range(5)))  # <class 'range'>


# itarable
for x in "python":
    print(x)

# o/p

# p
# y
# t
# h
# o
# n


for x in [1, 2, 3, "s", True, "hello"]:
    print(x)

  #  o/p
# 1
# 2
# 3
# s
# True
# hello


# while loop: let write a program which take in put and display it . it will run till user write "quit"


command = ""
while command.lower() != "quit":
    command = input(">")
    print("Echo", command)


# #o/p
# Echo e
# >r
# Echo r
# >we
# Echo we
# >quit
# Echo quit
# PS C:\Users\SUBHADIP KUNDU\Downloads\Desktop\pythonWithMosh>
