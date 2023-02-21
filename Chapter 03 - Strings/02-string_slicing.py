name = 'Shriyansh'

print(name[0])
print(name[1])
print(name[2])

# name[3] = z  --> Will not work

# [Step:Stop:Step]
print(name[0:4])         # Print from 0 to 3
print(name[:7])          # Print from 0 to 6
print(name[-4:-1])       # Print from -4 to -2
print(name[::])          # Print all the characters
print(name[::-1])        # Trick to reverse a string
print(name[::2])         # Print every 2nd character from the start
print(name[::-2])        # Print every 2nd character from the last
print(name[1:8:2])       # Print every 2nd character from the Index 1 to 8