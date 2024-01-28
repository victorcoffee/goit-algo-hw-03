# Модуль 3. Третє завдання

import re, os

# Функція нормалізує телефонний номер до стандартного формату,
# залишаючи тільки цифри та символ '+' на початку


def normalize_phone(phone_number: str) -> str:
    pattern = r"[+\d*]"
    matches = re.findall(pattern, phone_number)
    clean_number = "".join(matches)

    # Якщо міжнародний код відсутній, функція додає код '+38' і '+', якщо код без нього

    if len(clean_number) < 11:
        clean_number = "+38" + clean_number
    if 11 <= len(clean_number) < 13 and str(clean_number[0:3]) == "380":
        clean_number = "+" + clean_number

    return clean_number


os.system("cls")

# Приклади номерів
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
