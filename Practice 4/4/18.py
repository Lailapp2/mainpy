x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# отражённая точка
y2 = -y2

# параметр пересечения с y=0
t = -y1 / (y2 - y1)

xr = x1 + t * (x2 - x1)
yr = 0.0

print(f"{xr:.10f} {yr:.10f}")