def gen(n):
    for i in range(1,n+1):
        yield i*i

for x in gen(int(input())):
    print(x)