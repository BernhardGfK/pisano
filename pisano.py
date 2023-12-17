# A function to check if a number is prime
def is_prime(n):
  # Check if n is less than or equal to 1
  if n <= 1:
    # Return False
    return False
  # Loop from 2 to the square root of n
  for i in range(2, int(n**0.5) + 1):
    # Check if n is divisible by i
    if n % i == 0:
      # Return False
      return False
    # Return True
  return True

#This function works by checking if n has any factors other than 1 and itself. It uses the fact that if n is composite, it must have a factor less than or equal to its square root. This reduces the number of iterations needed to check for divisibility.

# A function to return the prime number decomposition of an integer
def prime_decomposition_list(n):
  # Initialize an empty list to store the prime factors
  factors = []
  # Start with the smallest prime factor 2
  d = 2
  # Loop until n is reduced to 1
  while n > 1:
    # Check if n is divisible by d
    if n % d == 0:
      # Add d to the list of factors
      factors.append(d)
      # Divide n by d
      n //= d
    else:
      # Increment d by 1
      d += 1
      # Return the list of factors
  return factors

# This function works by repeatedly dividing n by the smallest possible prime factor until it becomes 1. It uses a simple trial division algorithm, which has a time complexity of O(sqrt(n)) in the worst case.

# You want to have the prime factorization of an integer in the exponential form, such as 90 = 2^1 * 3^2 * 5^1. I can modify the function I wrote for you to achieve that. Here is one possible solution:

# A function to return the prime factorization of an integer in the exponential form
def prime_factorization(n):
  # Initialize an empty dictionary to store the prime factors and their exponents
  factors = {}
  # Start with the smallest prime factor 2
  d = 2
  # Loop until n is reduced to 1
  while n > 1:
    # Check if n is divisible by d
    if n % d == 0:
      # Increment the exponent of d in the dictionary
      factors[d] = factors.get(d, 0) + 1
      # Divide n by d
      n //= d
    else:
      # Increment d by 1
      d += 1
  # Return the dictionary of factors and exponents
  return factors

# This function works by using a dictionary to keep track of the prime factors and their exponents. It uses the same trial division algorithm as before, but instead of appending the factors to a list, it updates the dictionary values. It uses the get method to return the default value of 0 if the key is not in the dictionary.



# A function to calculate the Pisano period of n
def pisano(n):
  # Initialize the previous and current Fibonacci numbers modulo n
  prev = 0
  curr = 1
  # Loop until the period is found
  for i in range(n * n):
    # Update the previous and current numbers
    prev, curr = curr, (prev + curr) % n
    # Check if the period starts with 0, 1
    if prev == 0 and curr == 1:
      # Return the length of the period
      return i + 1

# Calculate and return Pisano Period
# The length of a Pisano Period for
# a given m ranges from 3 to m * m
def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
        = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

# A function to calculate the sum of all numbers smaller than M
# for which the Pisano period is k
def sum_pisano(M, k):
# Initialize the sum
  s = 0
  # Loop through all numbers from 1 to M
  for n in range(1, M):
    # Check if the Pisano period of n is k
    if pisano(n) == k:
      # Add n to the sum
      s += n
  # Return the sum
  return s

for n in (9, 19, 38, 76):
  print("pisano("+str(n)+")="+str(pisano(n)))

for n in range(2,100):
  if(is_prime(n)):
      print("pisano("+str(n)+")="+str(pisano(n)))

for n in range(2,100):
  if(pisano(n)==120):
      print("pisano("+str(n)+")="+str(pisano(n)))

print("The sum of all numbers smaller than 50 for which the Pisano period is 18 is "+str(sum_pisano(50, 18)))
print("The sum of all numbers smaller than 10^5 for which the Pisano period is 20 is "+str(sum_pisano(10**5, 20)))

# You can learn more about the Pisano period from Wikipedia https://en.wikipedia.org/wiki/Pisano_period or GeeksforGeeks https://www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/.
