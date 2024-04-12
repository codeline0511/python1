def month_days(y, m):
    if m == 4 or m == 6 or m == 9 or m =11:
        return 30
    elif m == 2:
        if is_leap_year(y):
            return 29
        else:
            return 28
    else:
        return 31

year = int(input('연도?'))
month = int(input('월?'))
ndays = month_days(year, month)

#미완성코드 
