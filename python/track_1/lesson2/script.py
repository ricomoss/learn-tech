#!/usr/bin/python
from utils.utils import wait

wait()

# Standard string
test_string = 'Strings start with \' and end with \'.'
print test_string

# Let's wait a moment before moving on
wait()

# Escape characters are needed occasionally
escapes = 'Notice the escape character is \\.'
print escapes
wait()

# Combine strings
test_string = 'Python cannot combine strings and numbers'
test_string2 = '...but it can combine strings with \'+\'.'
print test_string + test_string2
wait()

# Look at numbers
test_number = 10

# Try catch - if you expect possible failures
test_string = 'My test number is '
try:
    print test_string + test_number
except TypeError:
    print 'I told you.'
wait()

# But you can cast values
print test_string + str(10) + '.'
wait()

# Or, we can use .format to accomplish all casting for all types
print '{0}{1}.'.format(test_string, test_number)
wait()

# Play with .format - it will be used a lot
print '{0}{1} and {1} x {1} = {2}.'.format(
    test_string, test_number, test_number*test_number)
wait()

# if statement - determine the "truth" value of a statement
if True:
    print 'If'
wait()

# if-else - If true do "if", otherwise do "else"
if False:
    print 'If'
else:
    print 'Else'
wait()

# if-else if-else - A series of if conditions followed by else
if False:
    print 'If'
elif False:
    print 'First Else If'
elif True:
    print 'Second Else If'
else:
    print 'Else'
wait()

# Let's look at lists
test_list = list()
test_list.append('item 1')
test_list.append('item 2')
test_list.append('item 3')

# Indexed from zero
print test_list[0]
print test_list[1]
print test_list[2]
wait()

# A for loop is used to access every item in a list, dictionary or range of
# numbers
for item in range(0, 10):
    print item
wait()

for item in range(10, 20):
    print item
wait()

# Let's get something to loop through
test_list = ['Another', 'way', 'to', 'create', 'lists']
for item in test_list:
    print item
wait()

# Let's use a for loop to combine the items in the list to a single string
test_string = ''
for item in test_list:
    test_string += item + ' '

print test_string + '.'
wait()

# You noticed the trailing space.  That's not good.
test_string = ' '.join(test_list) + '.'
print test_string
wait()

# A while loop is like a for loop but it examines a changing value each time
# through the loop
tmp = 0
while tmp < 10:
    print tmp
    tmp += 1
wait()

# Exercise: Create a while loop to find a random number
item_found = False
search_value = '32'
import random
while not item_found:
    item = random.randint(1, 50)
    if str(item) == search_value:
        item_found = True
        print item
wait()

# Open a file for writing
my_file = open('example.txt', 'w')
my_file.write('line 1')
my_file.write('line 2')
try:
    my_file.write(3)
except TypeError:
    print 'Must write strings to files.'
my_file.close()
wait()

# Open the same file for reading
my_file = open('example.txt', 'r')
print my_file.readline()
my_file.close()
wait()

# Let's rewrite the file with newlines
my_file = open('example.txt', 'w')
my_file.write('line 1\n')
my_file.write('line 2\n')
my_file.close()

# Let's make sure the newlines worked
my_file = open('example.txt', 'r')
print my_file.readline()
my_file.close()
wait()

# Let's read all the lines instead of the first one
my_file = open('example.txt', 'r')
for line in my_file.readlines():
    print line
my_file.close()
wait()

# Let's add a line without having to rewrite the whole file
# Let's rewrite the file with newlines
my_file = open('example.txt', 'a')
my_file.write('line 3\n')
my_file.close()

# Let's read all the lines again
my_file = open('example.txt', 'r')
for line in my_file.readlines():
    print line
my_file.close()
wait()

import os
os.remove('example.txt')
