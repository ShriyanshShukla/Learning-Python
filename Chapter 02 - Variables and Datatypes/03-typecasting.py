a = "3456"

print(type(a))
# print(a + 7)   --> Error

a = int(a)       # It will !try to covert into your given datatype
print(a + 7)     # If a = "34fj95" and you use a = int(a), Program will give error
