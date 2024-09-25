# operators in python is used to perform operations on variables and values

# there are different types of operators in python
# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical operators
# 5. Identity operators
# 6. Membership operators
# 7. Bitwise operators

# Arithmetic operators
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

# example
x = 10
y = 5
print(x + y) # 15
print(x - y) # 5
print(x * y) # 50
print(x / y) # 2.0
print(x % y) # 0
print(x ** y) # 100000
print(x // y) # 2

# Assignment operators
# Assignment operators are used to assign values to variables

# example
x = 5
print(x) # 5

# example
x = 5
x += 3 # x = x + 3
print(x) # 8

# example
x = 5
x -= 3 # x = x - 3
print(x) # 2

# example
x = 5
x *= 3 # x = x * 3
print(x) # 15

# example
x = 5
x /= 3 # x = x / 3
print(x) # 1.6666666666666667

# example
x = 5
x %= 3 # x = x % 3
print(x) # 2

# example
x = 5
x //= 3 # x = x // 3
print(x) # 1


# example
x = 5
x **= 3 # x = x ** 3
print(x) # 125


# example
x = 5
x &= 3 # x = x & 3
print(x) # 1

# example
x = 5
x |= 3 # x = x | 3
print(x) # 7



# example
x = 5
x ^= 3 # x = x ^ 3
print(x) # 6

# example
x = 5
x >>= 3 # x = x >> 3
print(x) # 0

# example
x = 5
x <<= 3 # x = x << 3
print(x) # 40

# Comparison operators
# Comparison operators are used to compare


# example
x = 5
y = 3
print(x == y) # False

# example
x = 5
y = 3
print(x != y) # True

# example
x = 5
y = 3
print(x > y) # True


# example
x = 5
y = 3
print(x < y) # False

# example
x = 5
y = 3
print(x >= y) # True

# example
x = 5
y = 3
print(x <= y) # False

# Logical operators
# Logical operators are used to combine conditional statements

# example
x = 5
print(x > 3 and x < 10) # True

# example
x = 5
print(x > 3 or x < 4) # True

# example
x = 5
print(not(x > 3 and x < 10)) # False

# Identity operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location

# example
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # True

# example
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is y) # False


# example
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x == y) # True

# Membership operators
# Membership operators are used to test if a sequence is presented in an object

# example
x = ["apple", "banana"]
print("banana" in x) # True

# example

x = ["apple", "banana"]
print("pineapple" not in x) # True

# Bitwise operators
# Bitwise operators are used to compare (binary) numbers

# example

x = 10
y = 4
print(x & y) # 0 using bitwise and operator it will perform and operation on binary numbers of x and y set it =  1 and 0 = 0

# example
x = 10
y = 4
print(x | y) # 14 using bitwise or operator it will perform or operation on binary numbers of x and y set it =  1 and 0 = 1


# example
x = 10
y = 4
print(x ^ y) # 14 using bitwise xor operator it will perform xor operation on binary numbers of x and y set
# it =  1 and 0 = 1 and 0 and 1 = 1


# example
x = 10
print(~x) # -11 using bitwise not operator it will perform not operation on binary numbers of x set it =  1 and 0 = 0 and 1 = 0

# example
x = 10
print(x << 2) # 40 using bitwise left shift operator it will perform left shift operation on binary numbers of x set it =  1 and 0 = 10 and left shift 2 = 1000 = 8+32 = 40

# example
x = 10
print(x >> 2) # 2 using bitwise right shift operator it will perform right shift operation on binary numbers of x set it =  1 and 0 = 10 and right shift 2 = 0 = 0+2 = 2
