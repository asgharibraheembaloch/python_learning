# sets are unordered, mutaple, and with no dublicates

myset = {1,2,3}
print(myset)

# send does't allow dublicates
myset = {1,2,3,1,2}
print(myset)

   #OR

myset = set([1,2,3])
print(myset)

# sets are unordered does't allow dublicate
myset = set("Hello")
print(myset)

# this will recognise it as dictionary
myset = {}
print(type(myset))

# to regonise it as set use like that
myset = set()
print(type(myset))

# sets are mutable
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# to remove elements from sets
myset.remove(3)
print(myset)

# you can use discard method, benefit here it doesn't yield error if there is no element with provided value
myset.discard(4)
print(myset)

myset.discard(2)
print(myset)

# to clear entire set use this
myset.clear()
print(myset)

# use pop method if you want to remove first occuring element and also want to return it
myset = {1,2,3}
value = myset.pop()
print(value)
print(myset)

# to iterate over each element
myset = {1,2,3,4,5,6,7,8,9}
for i in myset:
    print(i)

# to check if there is an element inside set
if 10 in myset:
    print("yes")
else:
    print("no")

# to create union and intersection
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

# intersection will take elements that are found in both sets
i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)

# difference will return set with all elements from first set that are not in the second set
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diffA = setA.difference(setB)
print(diffA)

diffB = setB.difference(setA)
print(diffB)

""" the symetric difference method will return a set with all elements from
from setA and setB, but not the elements that are both in sets
"""

sym_diffA = setB.symmetric_difference(setA)
print(sym_diffA)

sym_diffB = setA.symmetric_difference(setB)
print(sym_diffB)

print(sym_diffA==sym_diffB)

# we can also update set on place with update
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
setA.update(setB)
print(setA)

# there is intersection update method that will update set on place with intersetion
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
setA.intersection_update(setB)
print(setA)

# there is also difference update method that will update set with difference
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
setA.difference_update(setB)
print(setA)

# there is also symmetric difference update method that will update set with difference in both
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
setA.symmetric_difference_update(setB)
print(setA)

# to check if a set is subset of another set
setA = {1,2,3,4,5,6}
setB = {1,2,3}
print(setA.issubset(setB)) # set A contains all element that are found in subset B
print(setB.issubset(setA))

# super set returns true if a set contains all elements that are in another set
setA = {1,2,3,4,5,6}
setB = {1,2,3}
print(setA.issuperset(setB))
print(setB.issuperset(setA))

# disjoint returns true if both sets a null intersectionn so no same elements
setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {7,8}

print(setA.isdisjoint(setB))
print(setB.isdisjoint(setA))
print(setA.isdisjoint(setC))

# copy set
setA = {1,2,3,4,5,6}
setB = setA

setB.add(7) # if you make changes will also be relected into setA
print(setB)
print(setA)

# if you want to make actually copy
setA = {1,2,3,4,5,6}
setB = setA.copy()

setB.add(7)
print(setB)
print(setA) # original set preserve its integrity

   #OR
setC = set(setA)

# frozen set another version of set with immutability
a = frozenset([1,2,3,4,5])
# you can not change frozen set after you created
a.add(6) # gives error 'frozenset' object has no attribute 'add'
a.remove(5) # gives error 'frozenset' object has no attribute 'remove'

# union and intersection method work on frozenset

