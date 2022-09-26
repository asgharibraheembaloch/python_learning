"""
    ###Collecyions###
    collections module implements special conatiner data type and provides
    alternatives with additional functionality compared to genertal bert and conatiner, like dictionaries
    lists or tuples, so we will talking about different types from the collections like
    counter, namedtuple, orderedDict, defaultdict, deque
"""

### Counter ####

"""
counter is container that stores the elements as dictionary keys and their counts as dictionary values
"""

from collections import Counter
a = "aaaaabbbcccccc"
my_counter = Counter(a)
print(my_counter)

print(my_counter.items()) # to get items
print(my_counter.keys()) # gives iterable over keys
print(my_counter.values()) # this gives iterable over values
print(my_counter.most_common(1)) # gives most common element within over collection dictionary
print(my_counter.most_common(2)) # gives the two most common types and return list of tuples of them
print(my_counter.most_common(1)[0]) # return tuple item
print(my_counter.most_common(1)[0][0]) # return most element name

# to return elements as its counts
print(my_counter.elements()) # return all commonly occuring elements
print(list(my_counter.elements())) # return list of all commonly occuring elements

### named tuple ####

"""
named tuple is easy to create and light weight object type
similar to struct
"""

from collections import namedtuple
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

### ordered dictionary ###

"""
orderd dictionary is just like regular dictionary but they remember the order
in which the item were inserted, new version of python have built in functionality
but if you use older version of python it is useful
"""
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

# new version of python just remembers the orders in which item were iserted
ordered_dict = {}
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

### default Dictionary ###
"""
default dictionary is like normal dictionary but difference is that it 
will have defult value if the key has not been set yet
"""
from collections import defaultdict

integer_dict = defaultdict(int) # will provide default integer value if it does't exist
float_dict =defaultdict(float) # will provide default float value if it does't exist
list_dict = defaultdict(list) # will provide default empty list if it does't exist

integer_dict['a'] = 1
integer_dict['b'] = 2
print(integer_dict['a'])
print(integer_dict['b'])
print(integer_dict['c']) # if key which is not in the dictionary provided then default integer value is used

### deque ###
""""
deque is double ended queue and it can be used to remove and add
elements from both ends
"""
from collections import deque

d = deque()
d.append(1)
d.append(2)

print(d)

# to append element at the left side
d.appendleft(3)
print(d)
d.pop() # this will remove last element
print(d) 
d.popleft()
print(d) # this will remove element from left side

# to remove all elements
d.clear()
print(d)

# to extend multiple item at the same time
d.extend([4,5,6])
print(d)

d.extendleft([1,2,3])
print(d)

# to rotate all element one place to the right
d.rotate(1)
print(d)

# to rotate all element two places to the right
d.rotate(2)
print(d)

# to rotate all element one place to the left
d.rotate(-1)
print(d)