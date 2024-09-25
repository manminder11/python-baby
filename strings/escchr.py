# escape character in python is backslash \ 
# 
# txt = "We are the so-called \"Vikings\" from the north."

# print(txt)

# # it will print We are the so-called "Vikings" from the north.
#
# # other escape characters

# txt = "Hello\nWorld!"
# print(txt)
# # it will print Hello in one line and World in the next line'

# txt = "Hello\tWorld!"
# print(txt)
# # it will print Hello and World with a tab space between them

# txt = "Hello \bWorld!"
# print(txt)
# # it will print HelloWorld! because \b is backspace so it will remove the space between Hello and World

# txt = "Hello \fWorld!"
# print(txt)
# # it will print Hello World! because \f is formfeed so it will remove the space between Hello and World

# txt = "Hello \rWorld!"
# print(txt)
# # it will print World! because \r is carriage return so it will remove the Hello and replace it with World

# txt = "Hello \oooWorld!"
# print(txt)
# # it will print Hello World! because \ooo is octal value so it will remove the space between Hello and World

# txt = "Hello \x48World!"
# print(txt)
# # it will print Hello HWorld! because \x48 is hexadecimal value so it will remove the space between Hello and World

# txt = "Hello \u0048World!"
# print(txt)
# # it will print Hello HWorld! because \u0048 is unicode value so it will remove the space between Hello and World

