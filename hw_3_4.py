# Модуль 3. Четверте завдання

import datetime, os


def get_upcoming_birthdays(users):
    # Створення пустого списку для результату роботи функції
    upcoming_birthdays = []

    today = datetime.datetime.today().date()
    # Призначення "сьогоднішньої" дати вручну для перевірки
    # today = datetime.date(2023, 12, 26)

    # Визначення кінця періода
    end_week = today + datetime.timedelta(days=7)

    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime.date(today.year, birthday.month, birthday.day)

        # Якщо день народження вже був у цьому році, визначаємо наступний
        if birthday_this_year < today:
            birthday_next_year = datetime.date(
                today.year + 1, birthday.month, birthday.day
            )
            nearest_birthday = birthday_next_year
        else:
            nearest_birthday = birthday_this_year

        # Перенесення привітання з вихідних  на понеділок
        if nearest_birthday.weekday() == 5:
            congratulation_date = nearest_birthday + datetime.timedelta(days=2)
        elif nearest_birthday.weekday() == 6:
            congratulation_date = nearest_birthday + datetime.timedelta(days=1)
        else:
            congratulation_date = nearest_birthday

        # Якщо день народження у найближчі 7 днів, то додаємо у список
        if today <= nearest_birthday < end_week:
            person_to_congratulate = {
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            }
            print(user["name"], birthday, birthday_this_year, congratulation_date)
            upcoming_birthdays.append(person_to_congratulate)

    return upcoming_birthdays


# Основна програма

os.system("cls")
users = [
    {"name": "Victor Coffee", "birthday": "1981.12.30"},
    {"name": "Sailor Moon", "birthday": "2001.07.09"},
    {"name": "Jane Smith", "birthday": "1990.12.27"},
    {"name": "John Doe", "birthday": "1985.01.01"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
