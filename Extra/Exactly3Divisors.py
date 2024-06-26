class Solution:
    def __init__(self):
        self.prime_squares = []
    def sieve(self, limit):
            is_prime = [True] * (limit + 1)
            p = 2
            while p * p <= limit:
                print(p,p*p)
                if is_prime[p]:
                    for i in range(p * p, limit + 1, p):
                        is_prime[i] = False
                        print(f"this is i {i} {is_prime[i]}")
                p += 1
            primes = [p for p in range(2, limit + 1) if is_prime[p]]
            return primes
    def exactly3Divisors(self, N):
            self.prime_squares = []
            # Generate primes up to sqrt(N)
            limit = int(N**0.5) + 1
            primes = self.sieve(limit)
            # Generate squares of these primes
            for prime in primes:
                square = prime * prime
                if square <= N:
                    self.prime_squares.append(square)
            return len(self.prime_squares)
x=int(input())
sol = Solution()
print(f"Ans {sol.exactly3Divisors(x)}")
# The Sieve of Eratosthenes is an ancient algorithm used to 
# find all prime numbers up to a specified integer. 
# It is one of the most efficient ways to identify 
# prime numbers for a given range and works based on the principle 
# of eliminating the multiples of each prime number starting from 2.