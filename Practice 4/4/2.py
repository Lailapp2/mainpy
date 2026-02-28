def even_generator(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

n = int(input())

first = True
for num in even_generator(n):
    if not first:
        print(",", end="")
    print(num, end="")
    first = False