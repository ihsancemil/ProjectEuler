def find_palindromes(digit):
    for i in range(10 ** (digit-1), 10 ** digit):
        for j in range(10 ** (digit -1), 10 ** digit):
            if str(i * j) == str(i * j)[::-1]:
                yield i* j

print max(find_palindromes(3))
