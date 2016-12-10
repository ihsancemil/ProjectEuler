def sum_square(max_num):
    return max_num * (max_num+1) * (2*max_num+1) / 6

def square_of_sum(max_num):
    return (max_num * (max_num+1) / 2) ** 2

print square_of_sum(100) - sum_square(100)
