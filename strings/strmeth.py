# methods of strings

# capitalize()	Converts the first character to upper case

a = "manminder"
print(a.capitalize())
# it will print Manminder because it will convert the first character to uppercase

# casefold()	Converts string into lower case
a = "MANMINDER"
print(a.casefold())
# it will print manminder because it will convert all the characters in lowercase

# center()	Returns a centered string
a = "manminder"
print(a.center(20))
# it will print "     manminder     " because it will center the string in the specified width

# count()	Returns the number of times a specified value occurs
a = "manminder"
print(a.count("m"))
# it will print 2 because m occurs twice in the string

# encode()	Returns an encoded version of the string
a = "manminder"
print(a.encode())
# it will print b'manminder' because it will encode the string

# endswith()	Returns true if the string ends with the specified value    
a = "manminder"
print(a.endswith("r"))
# it will print true because the string ends with r

# expandtabs()	Sets the tab size of the string
a = "manminder"
print(a.expandtabs(2))
# it will print manminder because it will set the tab size to 2

# find()	Searches the string for a specified value and returns the position of where it was found
a = "manminder"
print(a.find("m"))
# it will print 0 because m is at the 0th position

# format()	Formats specified values in a string
a = "manminder"
print("my name is {}".format(a))
# it will print my name is manminder    

# format_map()	Formats specified values in a string
a = "manminder"
print("my name is {name}".format_map({"name":a}))
# it will print my name is manminder

# index()	Searches the string for a specified value and returns the position of where it was found
a = "manminder"
print(a.index("m"))
# it will print 0 because m is at the 0th position

# isalnum()	Returns True if all characters in the string are alphanumeric
a = "manminder"
print(a.isalnum())
# it will print true because all the
# characters
# are alphanumeric

# isalpha()	Returns True if all characters in the string are in
# the alphabet
a = "manminder"
print(a.isalpha())
# it will print true because all the characters are in the alphabet

# isdecimal()	Returns True if all characters in the string are decimals