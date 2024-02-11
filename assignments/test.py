import matplotlib.pyplot as plt
import numpy as np
plt.style.use(["science", "grid", "notebook", "dark_background"])

def SieveOfEratosthenes(startnum: int, endnum: int) -> list:
    """Find all primes between startnum and endnum using Sieve of Erathmus algorithm
    Args:
        startnum (int): start number
        endnum (int): end number    
    Returns:
        list: list of primes between startnum and endnum"""
    # Initialize a list of with all elements as True
    isPrime: list = [True for _ in range(endnum+1)]
    # Loop through all the eleemnts from stratnum to sqrt(endnum)
    number = 2
    while number ** 2 <= endnum:
        # If number is not changed, it is prime
        if isPrime[number]:
            # Update all multiples of number
            for i in range(number ** 2, endnum + 1, number):
                isPrime[i] = False
        number += 1
    
    # Return all prime numbers between startnum and endnum
    return [i for i in range(startnum, endnum+1) if isPrime[i]]


# Test the function
startnum: int = 2
endnum: int = 100000000

primes = SieveOfEratosthenes(startnum, endnum)
r = theta = primes

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure(figsize = (10, 10))
plt.scatter(x, y, s = 1)
plt.show()