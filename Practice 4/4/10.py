def gen(lst,n):
    for _ in range(n):
        for x in lst:
            yield x

for x in gen(input().split(), int(input())):
    print(x,end=" ")