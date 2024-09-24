# formatting strings

# You can use the format() method to format strings.

a = "manminder"
b = "singh"
c = 21
print("my name is {} {} and my age is {}".format(a,b,c))
# it will print my name is manminder singh and my age is 21

# you can also use the index numbers inside the curly brackets to specify the order of the arguments
a = "manminder"
b = "singh"
c = 21
print("my name is {1} {0} and my age is {2}".format(a,b,c))
# it will print my name is singh manminder and my age is 21

# you can also use the named indexes inside the curly brackets to specify the order of the arguments

a = "manminder"
b = "singh"
c = 21
print("my name is {lname} {fname} and my age is {age}".format(fname=a,lname=b,age=c))

# it will print
# my name is singh manminder and my age is 21

# you can also use the f-string to format strings
a = "manminder"
b = "singh"
c = 21
print(f"my name is {a} {b} and my age is {c}")
# it will print my name is manminder singh and my age is 21
# f-string is a new way to format strings in python
# it is faster than other methods
# it is more readable
