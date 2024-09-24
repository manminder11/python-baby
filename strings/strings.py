print("manminder")
print('manminder')
# both are same 

# string can be enclosed in single quotes or double quotes

# qoutes inside the string

print("manminder's")
print("'manminder 's'")
print("my name is 'manminder singh '")

# assign string to a variable
a = "manminder"
print(a)



# multiline string
b = """manminder singh  is a doing software development at SAIT """
print(b)

# strings are arrays
a = "manminder"
print(a[1])
# it will print a because index start from 0 in python

# LOOPING THROUGH A STRING

for x in "manminder":
    print(x)
    # IT WILL PRINT EACH CHARACTER OF THE STRING IN A NEW LINE 

# STRING LENGTH
a = "manminder"
print(len(a))
# it will print 9 because there are 9 characters in the string

# check string
txt = "The best things in life are free!"
print("free" in txt) # one way to check if a certain phrase or character is present in a string, using the in keyword

if "free" in txt: # using if statement to check if a certain phrase or character is present in a string
    print("Yes, 'free' is present.")    


# it will print true because free is present in the string



# check if not present
txt = "The best things in life are free!"
print("expensive" not in txt) # one way to check if a certain phrase or character is not present in a string, using the not in keyword

if "expensive" not in txt: # using if statement to check if a certain phrase or character is not present in a string    
    print("Yes, 'expensive' is NOT present.")
# it will print true because expensive is not present in the string

