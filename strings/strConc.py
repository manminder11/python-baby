# concatination of strings is done by using + operator


a = "manminder"
b = "singh"
print(a+b)
# it will print manmindersingh

# you can also use the join() method to concatenate two strings

a = "manminder"
b = "singh"
print("my name is:".join([a,b]))
# it will print
# manminder singh
# join() method takes a list of strings as an argument and returns a string where the elements are joined by the separator provided in the join() method