import math

client = dict()


def DEPOSIT(name, sum):
    if (name in client):
        client[name] = client[name] + sum
    else:
        client[name] = sum


def WITHDRAW(name, sum):
    if (name in client):
        client[name] = client[name] - sum
    else:
        client[name] = 0
        client[name] = client[name] - sum


def BALANCE(name):
    if (name in client):
        return client[name]
    else:
        return ("ERROR")


def TRANSFER(name1, name2, sum):
    if (name1 in client and name2 in client):
        client[name1] = client[name1] - sum
        client[name2] = client[name2] + sum

    elif (name1 not in client and name2 not in client):
        client[name1] = 0
        client[name1] = client[name1] - sum
        client[name2] = sum

    elif (name1 not in client and name2 in client):
        client[name1] = 0
        client[name1] = client[name1] - sum
        client[name2] = client[name2] + sum
    elif (name1 in client and name2 not in client):
        client[name1] = client[name1] - sum
        client[name2] = sum


def INCOME(p):
    for name in client:
        if (client[name] > 0):
            client[name] = client[name] * (1 + (p / 100))
            client[name] = math.trunc(client[name])


operator = input("Ввеведите оперцию (чтобы закончить работы с банковской системой введите -end-) \n ")
while (operator != "end"):
    if (operator == "DEPOSIT"):
        name = input("Введите имя счета: ")
        sum = int(input("Введите сумму: "))
        DEPOSIT(name, sum)
        operator = input("Ввеведите оперцию (чтобы закончить работы с банковской системой введите -end-) \n ")

    elif (operator == "WITHDRAW"):
        name = input("Введите имя счета: ")
        sum = int(input("Введите сумму: "))
        WITHDRAW(name, sum)
        operator = input("Ввеведите оперцию (чтобы закончить работы с банковской системой введите -end-) \n ")

    elif (operator == "BALANCE"):
        name = input("Введите имя счета: ")
        print(BALANCE(name))
        operator = input("Ввеведите оперцию (чтобы закончить работы с банковской системой введите -end-) \n ")

    elif (operator == "TRANSFER"):
        name1 = input("Введите имя первого счета: ")
        name2 = input("Введите имя второго счета: ")
        sum = int(input("Введите сумму: "))
        TRANSFER(name1, name2, sum)
        operator = input("Ввеведите оперцию (чтобы закончить работы с банковской системой введите -end-) \n ")

    elif (operator == "INCOME"):
        procent = int(input("Введите число процентов: "))
        INCOME(procent)
        operator = input("Ввеведите оперцию (чтобы закончить работы с банковской системой введите -end-) \n ")

    else:
        print("Неизвестная оперция")
        operator = input("Ввеведите оперцию (чтобы закончить работы с банковской системой введите -end-) \n ")
