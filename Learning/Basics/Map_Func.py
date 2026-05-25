from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_duble = list(map(lambda x: x * 2, list(filter(lambda n: n % 2 == 0, nums))))


sum = reduce(lambda x, y: x + y, even_duble)
print(even_duble)
print(sum)
