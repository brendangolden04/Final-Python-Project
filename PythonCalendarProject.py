import sys

def get_year():
    year = int(input("Enter the year: "))
    if year <= 0:
        print("Year must be positive. ")
        sys.exit()
    return year

def get_starting_day():
    starting_day = int(input("Enter the day of the week for January 1st (0 for Sunday, 1 for Monday, ...): "))
    if starting_day < 0 or starting_day > 6:
        print("Day must be 0-6. ")
        sys.exit()
    return starting_day

def is_leap_year(the_year):
    if the_year % 4 != 0:
        return False
    if the_year % 100 != 0:
        return True
    if the_year % 400 != 0:
        return False
    return True

def print_month(name_month, num_days, starting_day):
    print(name_month)
    day_of_week = 0
    day_of_month = 1

    while day_of_week < starting_day:
        print("  ", end = "")
        day_of_week += 1
    while day_of_month <= num_days:
        if day_of_month < 10:
            print("  ", end = "")
        else:
            print(" ", end = "")
        print(day_of_month, end = "")
        day_of_month += 1

        if day_of_week == 6:
            print()
            day_of_week = 0
        else:
            day_of_week += 1
    print()
    if day_of_week != 0:
        print()
    return day_of_week

name_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
num_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = get_year()
if is_leap_year(year):
    num_month[1] += 1


next_day = get_starting_day()
for i, month in enumerate(name_month):
    next_day = print_month(month, num_month[i], next_day)

