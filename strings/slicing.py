# slicing is a way to extract a subsequence from a string


# slicing
a = "manminder"
print(a[2:5])
# it will print nmi because it will start from 2 and end at 5-1=4
# so it will print 2,3,4 index characters

# slice from the start
print(a[:5])
# it will print manmi because it will start from 0 and end at 5-1=4
# so it will print 0,1,2,3,4 index characters


# slice from the end
print(a[2:])
# it will print nminder because it will start from 2 and end at the end of the string
# so it will print 2,3,4,5,6,7,8 index characters

# negative indexing means starting from the end of the string and it starts from -1

print(a[-5:-2])
# it will print mind because it will start from -5 and end at -2-1=-3
# so it will print -5,-4,-3 index characters    # it will print mind
