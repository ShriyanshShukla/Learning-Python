a = 3
b = 4

# Arithmetic Operators
print("The value of 3 + 4 is", a + b)
print("The value of 3 - 4 is", a - b)
print("The value of 3 * 4 is", a * b)
print("The value of 3 / 4 is", a / b)

# Assignment Operators
a = 34
a += 2
a -= 2
a *= 2
a /= 2
print("The value of a is", a)     # The value will be in floating point number

# Comparison Operators
b = 4 > 7
print(b)
c = 14 >= 7
print(c)
a = 5 != 5
print(a)

# Logical Operators
bool_1 = True
bool_2 = False
print("The value of bool 1 and bool 2 is", (bool_1 and bool_2))
print("The value of bool 1 and bool 2 is", (bool_1 or bool_2))
print("The value of not bool 2 is", (not bool_2))

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.