ch = input("Введите символы:\n")
isnumber = [0,0,0,0,0,0,0,0,0,0] #Список количества встречаемых цифр
set = []
k=0
flag = False

while(ch != "." ): #Ввод сисволов покак не введена точка
    set.append(ch)
    ch = input()

for i in range(len(set)):#Нахождение количества вхождений цифр
    for j in set[i]:
        if j.isdigit():
            isnumber[int(j)] = isnumber[int(j)] + 1

for i in range (len(isnumber)): #Проверка на кратность вхождения
    if (isnumber[i] % 2 == 1 ):
        k = k + 1
        solonumber = i

for i in range (1,10):
    if((isnumber[i]>1) or (isnumber[i] == 1 and isnumber[0] == 0 ) or (isnumber[0] == 1)):#Условия вывода выполняются, если
        flag = True #Флаг отвечающий за выполнение условий
if(k>1 or not flag):
    print("NO")
else:
    print("YES")
    for i in range(9 , -1 , -1):
        for j in range(1, (isnumber[i] // 2) + 1):
            print(i, end='')
    if(k == 1):
        print(solonumber, end='')
    for i in range(0,10):
        for j in range(1 ,(isnumber[i] // 2) + 1):
            print(i, end='')

