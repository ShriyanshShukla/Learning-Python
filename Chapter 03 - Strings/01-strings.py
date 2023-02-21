a = 34  
b = 'Shriyansh'                  # Single quoted string
b = "Shriyansh"                  # Double quoted string
b = '''Shriyansh'''              # Triple quoted string
b = "Shriyansh's"                # We can use double quotes if we have single quotes in our strings and vice versa 
b = '''Shriansh's "Hammer"'''    # Use triple quotes if we have single and double both quotes in our strings
print(a,b)
print(type(a),type(b))

# String Concatenation
greeting = "Good Morning,"
name = 'Shriyansh'

c = greeting + name
print(c)
c = greeting + " " + name
print(c)