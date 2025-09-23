# Demonstrating Python Data Types

# 1. Integer (int) - Whole numbers
age = 21
print("age =", age, "| Type:", type(age))

# 2. Float (float) - Decimal numbers
pi = 3.14
print("pi =", pi, "| Type:", type(pi))

# 3. String (str) - Text data
name = "Bhagyashree"
print("name =", name, "| Type:", type(name))

# 4. Boolean (bool) - True/False values
is_student = True
print("is_student =", is_student, "| Type:", type(is_student))

# 5. List - Ordered, mutable collection
fruits = ["apple", "banana", "mango"]
print("fruits =", fruits, "| Type:", type(fruits))

# 6. Tuple - Ordered, immutable collection
coordinates = (10, 20)
print("coordinates =", coordinates, "| Type:", type(coordinates))

# 7. Set - Unordered collection with unique items
unique_numbers = {1, 2, 3, 3, 2}
print("unique_numbers =", unique_numbers, "| Type:", type(unique_numbers))

# 8. Dictionary - Key-Value pairs
student = {"name": "Bhagyashree", "age": 20, "course": "Python"}
print("student =", student, "| Type:", type(student))

# 9. NoneType - Represents absence of value
nothing = None
print("nothing =", nothing, "| Type:", type(nothing))

# we can identify the datatype of any variable using type() method
a = "Bhagyashree"
print(type(a))