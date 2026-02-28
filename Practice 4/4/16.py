from datetime import *

def p(s):
    d,t,z=s.split()
    sgn=1 if z[3]=='+' else -1
    h,m=map(int,z[4:].split(':'))
    return datetime.strptime(d+" "+t,"%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone(sgn*timedelta(hours=h,minutes=m)))

print(int((p(input())-p(input())).total_seconds()*-1))