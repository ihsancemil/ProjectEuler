def primes(max_num):
    prime_list = [True for i in range(max_num)]
    prime_list[0] = False
    prime_list[1] = False
    for i in xrange(max_num):
        if prime_list[i]:
            for j in xrange(2*i,max_num, i):
                prime_list[j] = False

    for i in range(max_num):
        if prime_list[i]:
            yield i

print sum(primes(2 * 10**6))
