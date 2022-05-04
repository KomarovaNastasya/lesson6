import pickle
import os
import class_date
import argparse
import random

parser = argparse.ArgumentParser(description="Это описание параметров")
parser.add_argument('-p', '--path', help='Путь к файлу')
parser.add_argument('-nQ', '--noQuestions', default=False, help='Запуск без вопросов')
args = parser.parse_args()

if args.noQuestions is False:
    question = input("Хотите сами задать дату? (Y/N) ").lower()
    if question == "y":
        day = input("Введите день ")
        month = input("Введите месяц ")
        year = input("Введите год ")
        setting_1 = class_date.Date(day, month, year)
    else:
        setting_1 = class_date.Date(random.randint(1, 31), random.randint(1, 12), random.randint(1, 99))
else:
    setting_1 = class_date.Date(random.randint(1, 31), random.randint(1, 12), random.randint(1, 99))

setting_2 = class_date.Date(random.randint(1, 31), random.randint(1, 12), random.randint(1, 99))

settings_array = [setting_1, setting_2]

with open(args.path, 'wb') as f:
    pickle.dump(settings_array, f)

if os.path.exists(args.path):
    print('Успешно сохранено! Чтобы посмотреть сохранение, запустите файл "get_date.py"')
