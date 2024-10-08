# Many Values to Multiple Variables
x, y ,z = "orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# have a collection of values in a list, tuple etc. 
# Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
