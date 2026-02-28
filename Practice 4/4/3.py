def gen(n):
    for i in range(0,n+1,12):
        yield i

for x in gen(int(input())):
    print(x, end=" ")