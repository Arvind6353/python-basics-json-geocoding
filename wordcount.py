fileName = 'app.txt'
handle = open(fileName)

counter = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words :
        counter[word] = counter.get(word,0) + 1

# largestCount = -1
# largestWord = None
# for k,v in counter.items() :
#     if v > largestCount :
#         largestCount = v
#         largestWord = k

# print(largestWord, largestCount)

# temp = []
# for k,v in counter.items():
#     temp.append((v,k))

# newtemp = sorted(temp, reverse=True)


newTemp = sorted([ (v,k) for (k,v) in counter.items()],reverse=True)

# top 4 
for v,k in newTemp[:4]:
    print(k,v)


