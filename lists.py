# lists: ordered, mutable, allows dublicate elements
from ast import ListComp


myList = ["banana", "cherry", "apple"]
print(myList)

myList2 = list()
print(myList2)

# list can contain multiple type of values

listWithTypes = [5, True, "apple"]
print(listWithTypes)

# list allows dublicate values
listWithDublicates = [5, True, "mango", "mango"]
print(listWithDublicates)

# element inside list can accessed via index number, index numbers starts from 0
firstElement = listWithDublicates[0]
secondElement = listWithDublicates[1]

print(f"{firstElement} is first element in the list at index 0", f"{secondElement} is second element in the list at index 1")

# get last element in the list, Note: -2 is the second last and so on
lastItem = myList[-1]
print(lastItem)

# to iterate over list
for element in myList:
    print(element)

# to check element is inside list, Note: change the values to check memberhsip of an element
if "orange" in myList:
    print("yes")
else:
    print("no")

# to check how many element inside list
print(len(myList))

# to append element inside list
myList.append("orange")
print(myList)

# insert an element at certain position
myList.insert(4, "lemon")
print(myList)

myList.insert(1, "blueberry")
print(myList)

# if you want to remove element from list
item = myList.pop() # Note: pop method by default removes last element from list and also return it
print(item)

print(myList)

# if you want specific element from list
myList.remove("lemon") # Note that remove doesn't return anything
print(item)

print(myList)

# to remove all element inside list

myList.clear()
print(myList)

# to reverse list items you can use reverse method
myList = ["banana", "cherry", "apple"]
myList.reverse()
print(myList)

# to sort list
myList = [1, 2, 3, -1 ,-2, -3 ,4, 5]
myList.sort()
print(myList)

# if you want your original list not to be change
originalList = [1, 2, 3, -1 ,-2, -3 ,4, 5]
sortedList = sorted(originalList)
print(sortedList)

print(originalList)

# create list with same values in multiple time
multipleList = [0] * 5
print(multipleList)

# concate list
myList1 = [1,2,3]
myList2 = [4,5,6]
concatList = myList1 + myList2

print(concatList)

# slice to get sub part of the list
myList = [1,2,3,4,5,6,7,8,9]
a = myList[1:5] # Note last index is excluded
print(a)

b = myList[:5] # all element from 0 to 5
print(b)

c = myList[1:] # element start at index 1 to end
print(c)

# slice list with step involved
d = myList[::2] # slice every second value in the list
print(d)

# nice trick to reverse list
e = myList[::-1] # get every one element from last order of the list
print(e)

# lists are by reference in memory
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
print(list_cpy)

list_cpy.append("lemon")
print(list_org)

# if you want to preserve original list
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org.copy()
list_cpy.append("lemon")
print(list_cpy)
print(list_org)

    # OR

list_cpy = list(list_org)

   # OR
list_cpy = list_org[:]

# list comprehension
# create a new list from existing in one line
myList = [1,2,3,4,5,6,7,8,9]
squaredList = [i*i for i in myList] # expression(i*i part) then after that is loop
print(squaredList)