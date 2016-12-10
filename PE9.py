def find_pythagorean(a, b):
    return (a**2 + b**2) ** (1.0/2)

def triplet(sum_num):
    for i in range(1, sum_num):
        for j in range(1, sum_num):
            if i + j + find_pythagorean(i, j) == sum_num:
                return i, j, find_pythagorean(i, j)

print int(reduce(lambda x, y: x * y, triplet(1000)))

