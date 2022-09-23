# dictionary is a data type consist of key-value pairs, unordered and mutable

# creating a dictionary
"""
dictionaries are created using key value pairs, seprated by colon
and then each key: value pair or item are sperated by ,
{"key": "value", key2: "value2"}
"""
import email


mydict = {"name": "asghar", "age": 28, "city": "islamabad"}
print(mydict)

     # OR

mydict2 = dict(name="faraz", age=38, city="karachi") # when we use dict to create we don't use "" quotes 
print(mydict2)

# access vlues from dictionary
value = mydict["name"]
print(value)

# dictionaries are mutable so can add values
mydict["email"] = "asghar@yahoo.com"
print(mydict)

# if provide new value to existing key it will be overitten
mydict["email"] = "asghar@gmail.com"
print(mydict)

# to delete value from dict
del mydict["email"]
print(mydict)

   #OR
mydict.pop("age")
print(mydict)

# to delete last item from dictionary we use popitem
mydict.popitem()
print(mydict)

# to check if a key inside dictionary
mydict = {'name': 'asghar', 'age': 28, 'city': 'islamabad'}

if "name" in mydict:
    print(mydict["name"])

# you can use try except block

try:
    print(mydict["name"]) # try to change with wrong key
except:
    print("error")

# loop through dictionary

#loop through keys

for key in mydict:
    print(key)

    # OR

for key in mydict.keys():
    print(key)

# keys() method return list with all keys inside dictionary
keys_list = mydict.keys()
print(keys_list)

# to return values from dictionary
for value in mydict.values(): # to return only value you must use dictionary values mathod
    print(value)

# to return both keys and values at same time
for key, value in mydict.items(): # to get key and value at same time use dictoinary items method
    print(key, value)

# to copy dictionary
mydict_cpy = mydict # both point same dictionary inside memory
print(mydict_cpy)

# dictionary is by refrence in memory so if we change inside mydict_cpy will change original dictionary
mydict_cpy["city"] = "karachi"
print(mydict)
print(mydict_cpy)

# so if you want to preserve integrity of the original
mydict_cpy = mydict.copy()
mydict_cpy["city"] = "islamabad"
print(mydict)
print(mydict_cpy)

      #OR
mydict_cpy = dict(mydict)

# to merge two dictionaries together
mydict = {"name":"asghar", "age": 28, "email": "asghar@xyz.com"}
mydict2 = dict(name="faraz", age=27, city="peshawar")

mydict.update(mydict2)
""" original dictionary is updated with new one with only keys that
    are similar in both and if there is new key value will then be added into dictionary
"""
print(mydict)

# you can use keys other than strings
mydict = {3: 9, 6: 36, 9: 87}
print(mydict)

value = mydict[3]
print(value)

# you can use tuple as key value inside dictionary
g1 = (1,2,3,4,5)
g2 = (6,7,8,9,10)

mygroup = {"group1": g1, "group2":g2}
mygroup2 = {g1: "group1", g2: "group2"} # you can also use tuple as keys in dictionary
print(mygroup)

# lists are hashable there cannot ne use as keys in dictionary, also because they are changes after creation
mylist = [8,7]
mydict = {mylist:15} # gives error "unhashable type"