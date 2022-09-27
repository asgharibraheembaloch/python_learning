#itertools: product, permutations, comibnations, accumulate, groupby, and infinite iterators

"""
itertools module is a collection of tools for handling iterators.
simply put iterators are data types that can be used in a for so for example most commin iterator is
list, itertool provide some advance tools like
product, permutations, comibnations, accumulate, groupby, and infinite iterators
"""
###product###
# will comppute cartesian product of the input iterables

from ast import Index
import imp
from inspect import indentsize
from itertools import product
import re
from sys import last_value
from tokenize import group
a = [1, 2]
b = [3, 4]
prod = product(a, b) 
print(prod)
print(list(prod))


l1 = [1, 2]
l2 = [3]

produc = product(l1, l2, repeat=2) 
print(produc)
print(list(produc))

###permuatations###

# promutations will return all possible ordering of an input
from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))

a = [1,2,3]
perm = permutations(a,2) # will limit permuatation with length of two permuation
print(list(perm))

# combination will return all possible cobination of an input
from itertools import combinations
a = [1,2,3,4]
comb = combinations(a,2) 
print(list(comb)) # note here that there is reptation for an element with cobination with itself

# combination with replacement will combine all possible combination including with itself
from itertools import combinations_with_replacement
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

# accumulated function makes an iterator that returns accumulated sums or any other binary function that is given as input
from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))

# we can also accumulate by multipication
from operator import index, indexOf, mul
acc = accumulate(a, func=mul)
print(a)
print(list(acc))

a = [1,2,5,3,4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))

# the group by function makes an iterator that returns keys and groups from iterable
from itertools import groupby
def smaller_than_3(x):
    return x<3

a = [1,2,3,4,5]
group_obj = groupby(a, key=lambda x: x<3) # smaller_than_3(x) is same as lambda just to provide intro to lambda
for key, value in group_obj:
    print(key, list(value))

 # another exmaple

persons = [{"name": 'asghar', "age": 28},
             {"name": 'ahmad',"age":25},
             {"name": 'nisar', "age": 25},
             {"name":'zia', "age":34}]

group_obj = groupby(persons, key=lambda x: x['age']) # group them by age
for key, value in group_obj:
    print(key, list(value))

###infinite iterators###
"""count, cycle, repeat"""

#count
from itertools import count, cycle, repeat, islice
import operator

for i in count(10):
    print(i)
    if i == 15: # if we don't check it will run infinitly
        break
    
# cycle

a = [1,2,3,2,3]

# this loop runs infinitly
""" 
for i in cycle(a):
    print(i) """

# we have limited the loop running time
for i in islice(cycle(a), 2*len(a)):  # Loops 10 times with a single value each time
    print(i)