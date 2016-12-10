def fibonacci_finder(max_num):
    fibonacci = [1, 1]
    while fibonacci[-1] + fibonacci[-2] < max_num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

even_fibonacci = [i for i in fibonacci_finder(4 * 10**6) if not (i%2)]
print sum(even_fibonacci)
