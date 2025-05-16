def chkPrime(no1):

    if (no1 <= 1):
        return False

    for i in range(2,int(no1 ** 0.5)+1):
        if(no1 % i == 0):
            return False
            break

    return True