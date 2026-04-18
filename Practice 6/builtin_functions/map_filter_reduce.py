# map_filter_reduce.py
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map: square each number
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# filter: keep even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce: sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)