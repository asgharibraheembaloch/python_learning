# tuples are ordered, immutable and allows dublicate
myTuple = ("asghar", 28, "Islamabad")# usually put values that belongs together, parenthesis are optional
print(myTuple)

singleValue = ("asghar") # cannot be considered tuple
print(type(singleValue))

tupleValue = ("asghar",) # you have put comma at the end
print(type(tupleValue))

# you can create tuple from iterable like this one
tupleFromIterable = tuple(["asghar", 28, "islamabad"])
print(tupleFromIterable)

# get values from tuple
item = tupleFromIterable[0]
print(item)

# get last value from tuple
myTuple = ("asghar", 28, "Islamabad")
lastVal = myTuple[-1]
print(lastVal)

# checking immuatability of tuple
myTuple[0] = "faraz" # this gives assignment error because tuple is immutable

# iterate through tuple
for element in myTuple:
    print(element)

# to check condition inside tuple
if "asghar" in myTuple:
    print ("yes")
else:
    print ("no")

# to check length of element inside tuple
my_name = ("a", "s", "g", "a", "r")
print(len(my_name))

# to count element inside tuple
print(my_name.count("a"))

# to find first occurance or index of particular element inside tuple
print(my_name.index("g"))

# to convert tuple into list
my_list = list(my_name)
print(my_list)

# convert list into tuple
my_tuple = tuple(my_list)
print(my_tuple)

# slicing tuple
a = (1,2,3,4,5,6,7,8,9)
b = a[2:5] # last index is excluded
print(b)

# unpacking tuple
my_tuple = "asghar", 28, "islamabad"

name, age, city = my_tuple # you must provide same number element as my_tuple
print(name)
print(age)
print(city)

# but if there too many values to unpack
my_tuple = (1,2,3,4,5,6,7,8,9)
i1, *i2, i3 = my_tuple
print(i1)
print(i3)
print(i2)

# some time tuple are more efficient than list
import numbers
import sys
from time import time
my_list = [0,1,2,"hello", True]
my_tuple = (0,1,2,"hello", True)
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))





