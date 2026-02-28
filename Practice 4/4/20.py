g=0
def outer():
    n=0
    def inner(s,v):
        global g; nonlocal n
        if s=="global": g+=v
        elif s=="nonlocal": n+=v
    for _ in range(int(input())):
        s,v=input().split()
        inner(s,int(v))
    print(g,n)
outer()