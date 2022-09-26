# strings are ordered immutable data type represented as text

# strings are represented with either single or double quotes
from multiprocessing.resource_sharer import stop
from typing import Concatenate
from unicodedata import decimal


my_string_double_quotes = "Hello World"
print(my_string_double_quotes)

my_string_single_quotes = 'Hello World'
print(my_string_single_quotes)

# error
my_string = 'I'm a programmer'
# corrections
my_string = 'I\'m a programmer'
print(my_string)
    # OR
print("I'm a programmer") # use double quoutes outside

# multiline strings are represented with triple quotes
my_string = """
Hello
world
""" 
print(my_string)
#OR
my_string = '''
Hello
world
'''
print(my_string)

# if you use backslash it won't consider another line

my_string = """
Hello \
World
asghar
"""

print(my_string)

# if you want to access characters or strings within text
my_string = "Hello world"
char = my_string[0]
print(char)

last_char = my_string[-1]
print(f"{last_char} is the last character")

second_last_char = my_string[-2]
print(f"{second_last_char} is the last second last character")

# strings are immutable so cannot change after you create it
my_string = "hello world"
my_string[0] = "H" # gives error 'str' object does not support item assignment

# you can apply slicing or you can get sub strings
substring = my_string[0:5] # 5 or (last) index is excluded
print(substring)

substring = my_string[:] # returns all charcters
print(substring)
substring = my_string[::1] # by default returns all step
print(substring)
substring = my_string[::2] # return every second character
print(substring)
substring = my_string[::-1] # it will reverse our string
print(substring)

# you can concatenate strings together
greeting = "Hello"
name = "asghar"
concatenate_string = greeting + " " + name
print(concatenate_string)

# you can iterate over string
for letter in concatenate_string:
    print(letter)

# to check if letter or charachter inside string
if 'e' in concatenate_string: # try to change letters
    print("yes")
else:
    print("no")

# you can also check substring
if 'ell' in concatenate_string:
    print("yes")
else:
    print("no")

# to remove or strip white space around text
my_string = '   asghar   '
my_name = my_string.strip()
print(my_name) # note you can't change original string because string is immutable

# UPPER case lower case

my_string = 'Hello World'
print(my_string.upper())
print(my_string.lower())

# to check if text start with character or substring
my_string = "Hello World"
print(my_string.startswith('H')) # returns boolean
print(my_string.startswith('Hello'))
print(my_string.startswith('World')) # because string does't start with 'World'

# to check if sentence ends with character or substring
print(my_string.endswith('World'))

# to find index of character or substring
print(my_string.find('o')) # returns first occuring index
print(my_string.find('World')) # returns from starting index
print(my_string.find('world')) # retruns -1 because does't found match and hence does't return index
print(my_string.find('WoRld')) # retruns -1 because does't found match and hence does't return index

# we can also find counts of characters within text
my_string = "Hello World"
print(my_string.count('o'))

# we can also replace strings
my_string = "Hello World"
print(my_string.replace("World", "Universe")) # original string remains same because string are immutable

# convert the string
my_string = 'how are you doing'
my_list = my_string.split() #split method by default split by space
print(my_list)

my_string = 'how,are,you,doing'
my_list = my_string.split(',') #split method use ',' delimiter here
print(my_list)

# convert back list into string again
new_string = ' '.join(my_list)
print(new_string)

# use treditional for loop method to create string from list 
my_list = ['a'] * 6
print(my_list)

my_string = ''
for i in my_list:
    my_string += i # this for loop is bad operation, it's very expensive operation because it each time create new my_string into memory
    print(my_string)

print(my_string)

     # OR
my_string = ''.join(my_list) # now it's much cleaner and faster
print(my_string)

"""
again use 
timer module 
for proof
"""

from timeit import default_timer as timer
# use treditional for loop method to create string from list 
my_list = ['a'] * 100000

start = timer()
my_string = ''
for i in my_list:
    my_string += i # this for loop is bad operation, it's very expensive operation because it each time create new my_string into memory
stop = timer()
print(stop-start)

     # OR
start = timer()
my_string = ''.join(my_list) # now it's much cleaner and faster
stop = timer()
print(stop-start)

"""
string formatting
   1. % old string formatting method
   2. format method
   3. f-string mathod
"""
# % old string formatting method

var = "asghar"
my_string = "the variable is %s" % var # 's' stands here for string and % here for formatting there at this place
print(my_string)

var = 3
my_string = "the variable is %d" % var # 'd' stands here for integer or decimal value and % here for formatting there at this place
print(my_string)

var = 3.14264
my_string = "the variable is %f" % var # 'd' stands here for floating point value and % here for formatting there at this place
print(my_string)

var = 3.14264
my_string = "the variable is %.2f" % var # .2f provide 2 digit floating point value after decimal point (.) 
print(my_string)

# format method

var = "asghar"
my_string = "the variable is {}".format(var) # {} use here to tell place holder after applying formating method on string
print(my_string)

var = 3
my_string = "the variable is {:d}".format(var) # 'd' stands here for integer or decimal value and % here for formatting there at this place
print(my_string)

var = 3.14264
my_string = "the variable is {:f}".format(var) # 'd' stands here for floating point value and % here for formatting there at this place
print(my_string)

var = 3.14264
my_string = "the variable is {:.2f}".format(var) # .2f provide 2 digit floating point value after decimal point (.) 
print(my_string)

var = 3.14264
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2) # .2f provide 2 digit floating point value after decimal point (.) 
print(my_string)

# f-string

var = "asghar"
print(f"the variable is {var}") # f before text tells that this code is formatted, {var} used here as place holder with variable provided 

var = 3
print(f"the variable is {int(var)}") # 'int' stands here for integer , operation here is at runtime


var = 3
print(f"the variable is {float(var)}") # float the value

var = 3.142566
print(f"the variable is {float(var): .2f}") # float value by two time


var = 3.14264
var2 = 6
print(f"the variable is {float(var):.2f} and {var}")