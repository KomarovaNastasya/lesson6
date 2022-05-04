import pickle
import os
import argparse

parser = argparse.ArgumentParser(description="Это описание параметров")
parser.add_argument('-p', '--path', help='Путь к файлу')
args = parser.parse_args()

if os.path.exists(args.path):
    with open(args.path, 'rb') as f:
        try:
            settings_array = pickle.load(f)
            setting_1 = settings_array[0].day, settings_array[0].month, settings_array[0].year
            setting_2 = settings_array[1].day, settings_array[1].month, settings_array[1].year
            print(f"Дата может быть не реальна!\n"
                  f"Ваша или случайная дата: {setting_1[0]}.{setting_1[1]}.{setting_1[2]}\n"
                  f"Просто случайная дата: {setting_2[0]}.{setting_2[1]}.{setting_2[2]}")
        except EOFError:
            print("Что-то пошло не так")
else:
    print('Файла не существует')
