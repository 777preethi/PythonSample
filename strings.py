print("Python Strings")
print("1. Square brackets used to access elements of the string")
a = "Hello, World"
print(a[2])
print("2. Substring gets the chacters between specific positions")
b = "Hello, World"
print(b[2:6])
print("3. The strip() method removes any whitespaces from the beginning or the end")
c = " Hello, World "
print(c.strip())
print("4. The len() method returns the length of a string")
d = "Hello, World"
print(len(d))
print("5. The lower() method returns the string in lower case")
e = "Hello, World"
print(e.lower())
print("6. The upper() method returns the string in upper case")
f = "Hello, World"
print(f.upper())
print("7. The replace() method replaces a string with anothe string")
g = "Hello, World"
print(g.replace("H","J"))
print("8. The split() method splits the string into substrings if it finds instances of the seperator")
h = "Hello, World"
print(h.split(","))
print("9. Python allows for command line input for user input using input() method")
print("Enter your name: ")
x = input()
print("Hello, " + x)