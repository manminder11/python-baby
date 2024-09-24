# global variables  is created outside of the function and can be used in any function

x = 10  

def myfunc():
  print(x)

myfunc()

# declaring  same variable inside the function
 
y = "awesome"

def myfunc():
    y = "fantastic"
    print("Python is " + y)

myfunc()

print("Python is " + y)


# global keyword
# if you want to create a global variable #inside a function
# , you can use the global keyword.

# it is used to create a global variable inside a function

def myfunc():
    global x # we are not saying global x = 5 we are just saying global x  so that we can use x outside the function
    x = "fantastic"

myfunc()

print("Python is " + x)