# Demonstrating Python Operators

# 1. Arithmetic Operators
a, b = 10, 3
print("Arithmetic Operators:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division (float)
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)  # Modulus (remainder)
print("a ** b =", a ** b)  # Exponent (power)

# 2. Comparison Operators (Relational)
print("\nComparison Operators:")
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater or equal
print("a <= b:", a <= b)  # Less or equal

# 3. Logical Operators
x, y = True, False
print("\nLogical Operators:")
print("x and y:", x and y)  # True if both are True
print("x or y:", x or y)    # True if at least one is True
print("not x:", not x)      # Negates the value

# 4. Assignment Operators
print("\nAssignment Operators:")
num = 5
print("num =", num)
num += 3   # num = num + 3
print("num += 3 →", num)
num -= 2   # num = num - 2
print("num -= 2 →", num)
num *= 4   # num = num * 4
print("num *= 4 →", num)
num /= 3   # num = num / 3
print("num /= 3 →", num)
num %= 3   # num = num % 3
print("num %= 3 →", num)

# 5. Bitwise Operators (work on binary values)
p, q = 5, 3  # 5 = 0101, 3 = 0011
print("\nBitwise Operators:")
print("p & q =", p & q)  # AND
print("p | q =", p | q)  # OR
print("p ^ q =", p ^ q)  # XOR
print("~p =", ~p)        # NOT (inverts bits)
print("p << 1 =", p << 1)  # Left shift
print("p >> 1 =", p >> 1)  # Right shift

# 6. Membership Operators
my_list = [1, 2, 3, 4]
print("\nMembership Operators:")
print("2 in my_list:", 2 in my_list)       # True if present
print("5 not in my_list:", 5 not in my_list)  # True if not present

# 7. Identity Operators
m = [1, 2, 3]
n = m
o = [1, 2, 3]
print("\nIdentity Operators:")
print("m is n:", m is n)    # True (same object)
print("m is o:", m is o)    # False (different objects, same content)
print("m is not o:", m is not o)
