"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open("foo.txt", 'r')
print(f.read())
f.close

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

b = open('bar.txt', 'w')
b.write('This is line 1.\nI need some diversity!\n')
b_value = ('This is gonna be a tuple converted\n', 35)
m = [value for value in b_value]
n = m[0]
o = m[1]
s = str(o)
b.write(n)
b.write(s)
b.close

b = open("bar.txt")
print(b.read())
b.close