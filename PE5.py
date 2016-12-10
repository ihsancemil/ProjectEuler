def lcm(max_num):
    num_list = range(2, max_num)
    for i in range(2, max_num):
        while 0 in [j%i for j in num_list]:
            is_divided = 0
            for num in num_list:
                if num%i == 0 and is_divided:
                    num_list[num_list.index(num)] /= i
                if num%i == 0 and not is_divided:
                    is_divided = 1
                    num_list[num_list.index(num)] /= i
                    yield i

print reduce(lambda i, j: i * j, lcm(20))
