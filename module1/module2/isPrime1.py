def checkForPrime1(n) :
    if n == 1 :
        return True
    for i in range(2,int(n/2)) :
        if n%i == 0 :
            return False;
    return True    
