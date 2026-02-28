import math

EPS = 1e-12

def dist_point_to_segment(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    if abs(dx) < EPS and abs(dy) < EPS:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    cx, cy = ax + t * dx, ay + t * dy
    return math.hypot(px - cx, py - cy)

def ang_norm(a):
    a %= (2 * math.pi)
    if a < 0:
        a += 2 * math.pi
    return a

def min_ang_diff(a, b):
    a, b = ang_norm(a), ang_norm(b)
    d = abs(a - b)
    return min(d, 2 * math.pi - d)

def tangent_angles(x, y, r):
    d = math.hypot(x, y)
    theta = math.atan2(y, x)
    if d <= r + EPS:
        # точка на окружности (или почти) -> касательная в этой точке, alpha=0
        return (theta, theta), 0.0
    alpha = math.acos(r / d)
    tlen = math.sqrt(d * d - r * r)
    return (theta - alpha, theta + alpha), tlen

r = float(input().strip())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# 1) Проверка: пересекает ли отрезок внутренность круга
dmin = dist_point_to_segment(0.0, 0.0, x1, y1, x2, y2)
straight = math.hypot(x2 - x1, y2 - y1)

if dmin >= r - 1e-12:
    # можно идти прямо (отрезок не заходит внутрь)
    print(f"{straight:.10f}")
else:
    # 2) Идём через касательные + дугу
    (a1, a2), la = tangent_angles(x1, y1, r)
    (b1, b2), lb = tangent_angles(x2, y2, r)

    best = float("inf")
    for aa in (a1, a2):
        for bb in (b1, b2):
            arc = r * min_ang_diff(aa, bb)
            best = min(best, la + lb + arc)

    print(f"{best:.10f}")