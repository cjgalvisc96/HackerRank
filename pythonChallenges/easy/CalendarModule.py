import calendar

def response(month, day, year):
    return calendar.day_name[calendar.weekday(year, month, day)].upper()

if __name__ == "__main__":
    month, day, year = map(int, input().split())
    print(response(month, day, year))
