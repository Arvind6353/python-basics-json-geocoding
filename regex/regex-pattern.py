import re

# keywords - * , ^ , +, ? , {} , [], \w, \W, \s, \S

def all_matches(text, pattern) :
    print(text)
    print(pattern)
    rx = re.compile(pattern)

    for matches in rx.finditer(text) :
        print(str(matches.start()) + ' - '+ str(matches.end()) + ' - ' + text[matches.start() : matches.end()] )

# zero or more occurrences of x(y)
all_matches('xyxyyxyyxyyyyxyyxyyx', 'xy*');

# one more occurrences of x(y)
all_matches('xyxyyxyyxyyyyxyyxyyx', 'xy+');

# find in the range starting with min count
all_matches('xyxyyxyyxyyyyxyyxyyx', 'xy{1,2}');

# find in the range
all_matches('xyxyyxyyxyyyyxyyxyyx', 'xy{2,}');

# avoid being greedy 
all_matches('xyxyyxyyxyyyyxyyxyyx', 'xy{2,}?');


# find alpha numeric  alphabet followed by number
all_matches('A6b7s8issi', '[a-zA-Z][0-9]');


# find non space 
all_matches('this is a test string ', '\S+');

# find space 
all_matches('this is a test string ', '\s+');

# find non alpanumeric 
all_matches('this is a -------test /..string for spl character and non alpha numeric', '\W+');

# find alphanumeric 
all_matches('this is a --test /..string for alpha numeric', '\w+');


# find alphabets not in the range of [a-i] ,not in (-) , not in (/) ,  not in (.) ,  and not (space) 
all_matches('this is a --test /..string for not in range condition ', '[^a-i-/.\s]');