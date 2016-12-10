def prime_factors(number):
    for i in xrange(2, number**1/2):
        if number == 1:
            return
        while (number % i == 0):
            number /= i
            yield i

print max(prime_factors(600851475143))
