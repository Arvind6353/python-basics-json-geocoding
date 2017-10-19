import re

print('pattern search --- ', re.search('pattern',' sample pattern check'))

searchRes = re.search('pattern',' sample pattern check')

print('search string --',searchRes.string)

print('found pattern --',searchRes.re.pattern)

print('start pattern pos --',(searchRes.start()))

print('end pattern pos --',(searchRes.end()))

# match  matches the string at the beginning

print(' matches only match at the beginning --', re.match('pattern','pattern match beginning'))

print(' matches doesnt match other than the beginning --', re.match('pattern','match pattern beginning'))


regx = re.compile('pattern')
print(' using compile --', regx.search('check for a particular regex pattern in the string'))


print('find all returns all the matched regex-pattern string (list) ---', regx.findall('check for a particular regex pattern in the string pattern'))