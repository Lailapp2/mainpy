def gen(n):
    for i in range(n,-1,-1):
        yield i

for x in gen(int(input())):
    print(x)