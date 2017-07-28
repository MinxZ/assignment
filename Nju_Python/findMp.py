from math import sqrt
def isprime(x):
    if x == 1:
        return 0
    k = int(sqrt(x))
    for j in range(2,k+1):
        if x%j == 0:
            return 0
    return 1

def findMp(num = 5):
    count = 0
    p = 2
    while 1:
        m = 2**p - 1
        if isprime(p) and isprime(m):
            print m
            count += 1
            if count == num: break
        p += 1

findMp()
