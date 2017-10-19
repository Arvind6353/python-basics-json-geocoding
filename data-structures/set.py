# allow only unique elements 

# keyword set


set1 = set(['one', 'two', 'three', 'two'])

print('set1 -',set1)

set2 = set(['four', 'two'])

print('set2 -', set2)

# set operations

#add
set1.add('five')

print('after adding "five" to the set1 -', set1)
print('set2 -', set2)


#union
print('union of set1 and set2 -',set.union(set1,set2))

#intersection
print('intersection of set1 and set2 -', set.intersection(set1,set2))

#difference 
print('difference between set1 and set2 -', set.difference(set1,set2))

print('difference between set2 and set1 -', set.difference(set2,set1))


#sets are assigned by reference - shallow copy
set3 = set2
print('set3 assigned from set2', set3)
set2.add('six')

print('after adding "six" in set2 -',set2)
print('set3 has reference to set2 and hence set3 is also updated -',set3)
