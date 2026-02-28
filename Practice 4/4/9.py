def gen(n):
    for i in range(n+1):
        yield 2**i

for x in gen(int(input())):
    print(x, end=" ")