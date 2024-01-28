# Модуль 3. Перше завдання

import datetime
import os


def get_days_from_today(date):
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        today = datetime.datetime.today()
        # delta = today.date() - date.date()
        delta = today - date
        return delta.days
    except:
        print("The date must be specified in the format YYYY-MM-DD")
        return


os.system("cls")

# Test cases

# x_day = "2022-02-23"
# print(get_days_from_today(x_day))

# future_day = "2025-05-12"
# print(get_days_from_today(future_day))

# x_day = "2022/02/23"
# print(get_days_from_today(x_day))

while True:
    someday = input("Input any date: ")
    print(get_days_from_today(someday))
