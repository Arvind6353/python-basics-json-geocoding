
# regex 
# keywords - search , findall ,  match , compile

import re

# search for pattern . if found return match else return None

print('pattern search --- ', re.search('pattern',' sample pattern check'))

searchRes = re.search('pattern',' sample pattern check')

print('search string --',searchRes.string)

print('found pattern --',searchRes.re.pattern)

print('start pattern pos --',(searchRes.start()))

print('end pattern pos --',(searchRes.end()))


# match - matches the string at the beginning

print(' matches only match at the beginning --', re.match('pattern','pattern match beginning'))

print(' matches doesnt match other than the beginning --', re.match('pattern','match pattern beginning'))

# create regex obj by passing the pattern 
regx = re.compile('pattern')
print(' using compile --', regx.search('check for a particular regex pattern in the string'))

# find all returns all matched pattern string as list 
print('find all returns all the matched regex-pattern string (list) ---', regx.findall('check for a particular regex pattern in the string pattern'))

# return all the matched string
print(re.findall('[0-9]',"asd12323"))

# check for occurrence and return the result. if not found return none 
print(re.search('[0-9]',"asd"))

# check for occurrence and return when the pattern matches the first occurrence .[ here 's']
print(re.search('[asdf]',"pwosdd"))
