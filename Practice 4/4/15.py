from datetime import datetime, timedelta, timezone

def parse(s):
    d, tz = s.split()
    sign = 1 if tz[3] == '+' else -1
    h, m = map(int, tz[4:].split(':'))
    return datetime.strptime(d, "%Y-%m-%d").replace(
        tzinfo=timezone(sign * timedelta(hours=h, minutes=m))
    )

def leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

birth = parse(input().strip())   # midnight in birth tz
now = parse(input().strip())     # midnight in current tz

def bday_in_year(year):
    m, d = birth.month, birth.day
    if m == 2 and d == 29 and not leap(year):
        d = 28
    return datetime(year, m, d, tzinfo=birth.tzinfo)  # midnight in birth tz

target = bday_in_year(now.year)

# сравниваем реальные моменты времени
if target.astimezone(timezone.utc) < now.astimezone(timezone.utc):
    target = bday_in_year(now.year + 1)

t = (target.astimezone(timezone.utc) - now.astimezone(timezone.utc)).total_seconds()

if t <= 0:
    print(0)
else:
    print(int((t + 86400 - 1) // 86400))  # ceil(t/86400)