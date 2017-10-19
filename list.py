
#list is mutable

#keyword - list
import functools

list1 = [ 1,2 ,3 ,4]


list1.append(6)

print('appended list' , list1)

print('first four elements of the list', list1[0:4])

#adding new element to the list

list1[len(list1) : ] = [99]

print('new list', list1)

# can modify content of the list .

list1[0] = 5

print('modified list', list1)


def mulby2(x) :
    return x*2;


print ('using map with lambda', list(map( lambda x : x*2, list1 ) ))

print ('using map with function def', list(map( mulby2, list1 ) ))


print ('using filter with lambda', list(filter( lambda x : x<5, list1 ) ))


print ('using reduce with lambda',functools.reduce(lambda x,y : x*y , list1[0:4]))