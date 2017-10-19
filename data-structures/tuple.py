# tuples are immutable
#keyword - tup;e

#ways to create tuple
tup1 = (1,2,3)

print('tuple1', tup1)

# create tuple as comma separated
tup2 = 1,2,3

print('tuple2', tup2)


#slice operation on tuple
print('sliced out tuple1',tup1[0:2])

print('length of the tuple1',len(tup1))


#iterate over each tuple element
print('iterate over tuple')
for k in tup1:
    print(k)
print('-----end of iteration------')


print('max of tuple', max(tup1))

print('min of tuple', min(tup1))

print('check for existence of 3 in tup1', 3 in tup1)

print('check for existence of 999 in tup1', 999 in tup1)
