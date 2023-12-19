import math

#Function that determines if a number is prime or not
#Input: number
#Output: True or False
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        if n%2 == 0:
            return False
        for i in range(3,int(math.sqrt(n))+1,2):
            if n%i == 0:
                return False
        return True
#Function that returns the prime factors of a number
#Input: number
#Output: list of prime factors
def primeFactors(n):
    pf = []
    i = 2
    while n>1:
        if n%i == 0:
            pf.append(i)
            n = n//i
        else:
            i+=1
    return pf

#Function that returns all divisors of a number
#Input: number
#Output: list of divisors
def divisors(n):
    div = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            div.append(i)
            div.append(n//i)
    return div

#Function that returns all divisors of a number less than its square root
#Input: number
#Output: list of divisors
def ddivisors(n):
    div = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            div.append(i)
            div.append(n//i)
    return div
#Function that returns all primes less than a numbe
#Input: number
#Output: list of primes
def oddPrimesLessThan(n):
    primes = []
    for i in range(3,n,2):
        if isPrime(i):
            primes.append(i)
    return primes

#Functions that returns all subsets of a list
#Input: list
#Output: list of lists
def subs(l):
    if l == []:
        return [[]]
    x = subs(l[1:])
    return x + [[l[0]] + y for y in x]

# Function that checks whether d+n/d is prime for all divisors d of 
# Input: number
# Output: True or False
def isdpdprim(n):
    div = ddivisors(n)
    for i in div:
        if not isPrime(i+n//i):
            return False
    return True

primes=oddPrimesLessThan(100)
s=0
for i in subs(primes):
    # multiply all elements of i and 2
    prod = 2
    for j in i:
        prod *= j
    if prod <100000000 and isdpdprim(prod):
        print(prod)
        s+=prod
print("Sum: ",s)
#exit(0)

for i in range(2,100000,2):
    if isdpdprim(i):
        print(i)
        print(divisors(i)) 
        print(primeFactors(i)) 
#exit(0)

s=0
for i in range(2,100000000,2):
    if(i%100000 == 0):
        print("intermediate: ",i)
    if isdpdprim(i):
        s+=i
print("Sum: ",s)
#exit(0)

for i in range(1,100):
    if isPrime(i):
        print(i)

for i in range(1,100):
    print(divisors(i)) 
