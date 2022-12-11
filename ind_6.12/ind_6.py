import csv
import pandas as pd

def pods(myDict, lookup):
    for k, v in myDict.items():
        if lookup == v:
            return k


FIRST_PATH = '12 - 1.csv'
SECOND_PATH = '12 - 2.csv'

month = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь',
         10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

points = int(input("Введите количество набранных баллов "))

date_start = input("Введите диапозон дат на которыйх будет происходить поиск: ")
date_end = input(" ")
date_start = date_start.split()
date_end = date_end.split()
month_start = pods(month, date_start[1])
month_end = pods(month,date_end[1])


def main():
    with open(FIRST_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data_first = list(reader)
        count = 0
    with open(SECOND_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data_second = list(reader)

    answers = {}



    for row in data_second:
        mark = row["Оценка/100,00"]
        mark = mark.replace(',', '.')
        if mark == '-':
            if answers.get(row["Адрес электронной почты"]):
                answers[row["Адрес электронной почты"]]['Даты повторных попыток'].append(row["Тест начат"][:-7])
        elif float(mark) == points:
            date_of_test = row["Завершено"].split()
            month_test = pods(month, date_of_test[1])
            if (date_of_test[0] >= date_start[0] and date_of_test[1] == date_start[1]) or (
                    date_of_test[0] <= date_end[0] and date_of_test[1] == date_end[1]) or (
                    month_test in range(int(month_start) + 1, int(month_end))):
                if answers.get(row["Адрес электронной почты"]):
                    answers[row["Адрес электронной почты"]]['Даты повторных попыток'].append(
                        row["Тест начат"][:-7])
                else:
                    answers[row["Адрес электронной почты"]] = {}
                    answers[row["Адрес электронной почты"]] |= row

    people = []
    for row in answers:
        people.append([answers[row]['Фамилия'],answers[row]['Имя'],answers[row]['Адрес электронной почты'],answers[row]['Завершено']])
    people.sort()
    print(people)


if __name__ == '__main__':
    main()
