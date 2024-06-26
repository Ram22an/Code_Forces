
def count_numbers_with_exactly_3_divisors(N):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    count = 0
    i = 2
    while i * i <= N:
        if is_prime(i):
            if i * i <= N:
                count += 1
        i += 1
    
    return count
x=int(input())
print(count_numbers_with_exactly_3_divisors(x))

# The reason we only need to check up to the square root of 
# N is that a number has exactly 3 divisors if and only if it is the square of a prime number.
# A number x has exactly 3 divisors if and only if x is of the form p^2, where p is a prime number.
# The divisors of p^2 are:1, p, and p^2.Hence, exactly 3 divisors.
# For example, if N=100,then under root 100 =10. We only need to check prime numbers up to 10. 
# The squares of these primes (2, 3, 5, 7) are 4, 9, 25, and 49 respectively, all of which are ≤100
# https://chatgpt.com/share/e87d55d0-59b2-4716-9dfd-2fd1d35284c6
