from datetime import datetime, timedelta, timezone

def parse(line):
    date_part, tz_part = line.split()
    sign = 1 if tz_part[3] == '+' else -1
    hh, mm = map(int, tz_part[4:].split(":"))
    offset = timezone(sign * timedelta(hours=hh, minutes=mm))
    return datetime.strptime(date_part, "%Y-%m-%d").replace(tzinfo=offset)

d1 = parse(input().strip())
d2 = parse(input().strip())

diff_seconds = abs((d1 - d2).total_seconds())
print(int(diff_seconds // 86400))