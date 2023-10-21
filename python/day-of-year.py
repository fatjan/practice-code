def day_of_year(self, date: str) -> int:
    month_day = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    days_amount = []
    res = 0
    for _, val in month_day.items():
        res += val
        days_amount.append(res)
    
    month = int(date[5:7])
    day = int(date[8:])
    if month == 1:
        return day

    year = int(date[:4])
    def is_leap_year(year):
        if (year % 400 == 0) and (year % 100 == 0):
            return True
        elif (year % 4 ==0) and (year % 100 != 0):
            return True
        else:
            return False
    
    days = days_amount[month-2] + day
        
    if is_leap_year(year) and month > 2:
        days += 1
    
    return days

print(day_of_year(1, "2019-01-09"))
print(day_of_year(1, "2019-02-10"))
print(day_of_year(1, "2003-03-01"))
print(day_of_year(1, "2004-03-01"))
print(day_of_year(1, "1900-03-01"))