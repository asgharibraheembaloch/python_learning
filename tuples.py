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