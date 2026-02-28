import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx, dy = x2 - x1, y2 - y1
L = math.hypot(dx, dy)

# если отрезок - точка
if L == 0.0:
    print("0.0000000000")
    raise SystemExit

a = dx*dx + dy*dy
b = 2.0 * (x1*dx + y1*dy)
c = x1*x1 + y1*y1 - r*r

D = b*b - 4*a*c
eps = 1e-12

def inside(x, y):
    return x*x + y*y <= r*r + eps

if D < -eps:
    # либо весь внутри, либо весь снаружи
    ans = L if (inside(x1, y1) and inside(x2, y2)) else 0.0
else:
    D = max(0.0, D)
    s = math.sqrt(D)
    t1 = (-b - s) / (2*a)
    t2 = (-b + s) / (2*a)
    if t1 > t2:
        t1, t2 = t2, t1

    # внутри круга для t в [t1, t2], пересекаем с [0,1]
    tin = max(0.0, t1)
    tout = min(1.0, t2)

    if tout <= tin + eps:
        ans = L if (inside(x1, y1) and inside(x2, y2)) else 0.0
    else:
        ans = (tout - tin) * L

print(f"{ans:.10f}")