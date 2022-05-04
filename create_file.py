import os
import argparse

parser = argparse.ArgumentParser(description="Это описание параметров")
parser.add_argument('-n', '--name', default='User', help="Имя пользователя")
parser.add_argument('-p', '--path', default="file.txt", help='Файл')
parser.add_argument('-cF', '--createFile', action='store_true', help='Создание файла при его отсутствии')
parser.add_argument('-nQ', '--noQuest', default=False, help='Запуск без вопросов')
args = parser.parse_args()

print(f"Hola, {args.name}!")
# print(os.getcwd())

answer = ""


def createfile():
    with open(args.path, "w+", encoding='UTF-8') as f:
        f.write('Файл')
    return


if not os.path.exists(args.path):
    if args.createFile:
        print("Tакого файла нет, создаю.")
        createfile()
    else:
        if not args.noQuest:
            answer = input("Такого файла нет. Хотите его создать? (Y/N)\n").capitalize()
        if answer == "Y" or args.noQuest:
            createfile()
        else:
            print("Такой файл продолжает не существовать.")
            exit(0)

else:
    print("У вас есть этот файл")

answer = ""

if not args.noQuest:
    answer = input("Хотите удалить файл? (Y/N)\n").capitalize()
if answer == "Y" or args.noQuest:
    print("Удаляю")
    os.remove(args.path)
else:
    print("Хорошо, файл оставлен в покое.")
    exit(0)
