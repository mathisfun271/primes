import time
import math

from random import sample,randint,randrange, getrandbits
from math import gcd,log,floor,ceil

def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=1024):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

def primes():
    print("Record to: \n100K: 0 seconds\n1 Million: 0 seconds\n10M: 16 sec\n100M: 372 sec")
    un = int(input("Up to (): "))
    n = math.ceil(un**0.5)
    st = time.time()
    p = [2,3]
    cp = [0.5]
    sp = []
    running = True
    y = 0
    pp = 3 #Previous Prime
    lp = 2 #Lower Prime
    up = 3 #Upper Prime
    while running:
        for x in range(round((lp**2+1)/2),round((up**2-1)/2)):
            val = 2*x+1
            pr = True
            for z in sp:
                if val % z == 0:
                    pr = False
                    break
            if pr:
                cp.append((val-pp)//2)
                pp = val
        sp.append(up)
        if up >= n:
            running = False
        lp += int(2*cp[y])
        y+=1
        up += int(2*cp[y])
        
    print("%d seconds" % (time.time() - st))
    return(cp)

cp = primes()
def primeN(n):
    if n > len(cp)+1:
        return(0)
    elif n >2:
        val = 3
        for x in range(1,n-1):
            val += 2*cp[x]
        return val
    else:
        return n+1
def isPrime(n):
    pr = True
    sqrtn = n**0.5
    for x in range(1,len(cp)+2):
        p = primeN(x)
        if n % p == 0:
            pr = False
        if p > sqrtn:
            break
    if pr:
        if n <= primeN(len(cp)+1)**2:
            return True
        else:
            return "too big"
    else:
        return False
def prevPrime(n):
    running = True
    t = 0
    if n % 2 ==0:
        t = n-1
    else:
        t = n-2
    while running:
        if isPrime(t)==True:
            return t
        t-=2
        
def nextPrime(n):
    running = True
    t = 0
    if n % 2 ==0:
        t = n+1
    else:
        t = n+2
    while running:
        if isPrime(t)==True:
            return t
        t+=2
        
        







    
