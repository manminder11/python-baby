# NUMBERS
X =1   # int
X =1.0 # float
X =1j  # complex
X = True # bool
X = None # None


print (type(X)) # <class 'bool'>
print (type(X)) # <class 'NoneType'>
print (type(X)) # <class 'int'>
print (type(X)) # <class 'float'>
print (type(X)) # <class 'complex'>


# type conversion

# int to float
x = 1
y = float(x)
print(y) # 1.0

# float to int
x = 1.0
y = int(x)
print(y) #\ 1

# int to complex
x = 1
y = complex(x)
print(y) # 1j


# complex to int
x = 1j
# y = int(x) # TypeError: can't convert complex to int
# print(y)


# complex to float
x = 1j
# y = float(x) # TypeError: can't convert complex to float
# print(y)


# float to complex
x = 1.0
y = complex(x)
print(y) # 1j


# bool to int
x = True
y = int(x)
print(y) # 1

# int to bool
x = 1
y = bool(x)
print(y) #

# bool to float
x = True
y = float(x)
print(y) # 1.0

# float to bool
x = 1.0
y = bool(x)
print(y) #

# bool to complex
x = True
y = complex(x)
print(y) # (1+0j)

# complex to bool
x = 1j
# y = bool(x) # TypeError: can't convert complex to bool
# print(y)

# RANDOM NUMBER
import random
print(random.randrange(1,10)) # 1-9



