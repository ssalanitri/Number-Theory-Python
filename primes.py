import primesieve

def next_prime(p):
    print(primesieve.nth_prime(p))
    
    
##Lista los primeso n primos.
def list_primes(n):
    for i in range(n):
        print(primesieve.nth_prime(i))



list_primes(10**6)