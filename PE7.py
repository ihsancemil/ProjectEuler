def is_prime(a):
    if a == 2:
        return 1
    if a <= 1:
        return 0
    for i in range(2, int(a**(1.0/2)+1)):
        if a%i == 0:
            return 0
    return 1

def primes(count):
    i = 1
    prime_counter = 0
    while prime_counter != count:
        if is_prime(i):
            prime_counter += 1
        i += 1
    return i-1

print primes(10001)
