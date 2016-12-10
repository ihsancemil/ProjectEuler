def divide_rule(max_num, step):
    max_num -= 1
    return step * (max_num/step) * ((max_num/step) + 1) / 2

divide_three = divide_rule(1000, 3)
divide_five = divide_rule(1000, 5)
divide_fifteen = divide_rule(1000, 15)

print divide_three + divide_five - divide_fifteen
