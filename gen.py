from datetime import timedelta,datetime,date

def gen(startDate, endDate, step=timedelta(), inclusive=True):
    sdate = datetime.strptime(startDate, '%d.%m.%Y')
    edate = datetime.strptime(endDate, '%d.%m.%Y')
    if step.days > 0:
        while sdate < edate:
            yield sdate
            sdate = sdate + step
    elif step.days < 0:
        while sdate > edate:
            yield sdate
            sdate = sdate + step
    if inclusive and sdate == edate:
        yield sdate
fy = gen('30.04.1998', '11.05.2019', step=timedelta(), inclusive=True)
print(next(fy))

