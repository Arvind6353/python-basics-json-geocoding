import re

# return the matched string
print(re.findall('[0-9]',"asd12323"))

# check for occurrence and return the result. if not found return none 
print(re.search('[0-9]',"asd"))

# check for occurrence and return when the pattern matches the first occurrence .[ here 's']
print(re.search('[asdf]',"sdd"))
