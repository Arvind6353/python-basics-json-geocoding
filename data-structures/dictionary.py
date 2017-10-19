# key value pair

# keyword - dict

dict1 = { 'name' : 'ad', 'age' :2}

print('dictionary dict1 -',dict1)

#get specific value from dict
print('get the value of the name key from dict1 -',dict1['name'])

# create new item in dictionary

dict1['address'] = 'address1'

print('updated dictionary dict1 -',dict1)

#get list of keys
print('keys of the dict1 -', dict1.keys())

#get list of values
print('values of the dict1 -',dict1.values())

# = assignment assigns the ref not the value - shallow copy
dict2 = dict1

print('dictionary dict2 -', dict2)

print('compare dictionaries dict1 and dict2 -' , dict2 == dict1)

# modify dict1 - but it updates in dict2 as well

dict1['age'] = 1000

print('modified dict1 - ', dict1)
print('through ref dict2 also gets changed based on dict1 - ', dict2)

print('compare again the dictionaries dict1 and dict2 -' , dict2 == dict1)