# how to swap diff varialbes

print("enter the first number") 
x = int(input())
print("enter the second number")
y = int(input())

print("x  is", x)
print("y is", y)

# using extra variable
temp = x
x = y
y = temp

print("x  is", x)
print("y is", y)

# shortcut of python
x, y = y, x

print("x  is", x)
print("y is", y)

# using xor
x = x ^ y
y = x ^ y
x = x ^ y

print("x  is", x)
print("y is", y)
