file = open("py.txt")
fPrev = []
fNow = []
fAnswer =[0,0,0,0]
line = file.readline()
for i in line:
    if i.isnumeric():
        fNow.append(int(i))

while True:

    line = file.readline()

    if not line:
        break

    fPrev = fNow
    fNow = []

    for i in line:
        if (i.isnumeric()):
            fNow.append(int(i))

    if fPrev[4] == 0 and fPrev[5] == 0:
        continue
    else:
        if fNow[4] != 0:
            for i in range(0,fPrev[4]+1):
                for j in range(0,4):
                    if fPrev[j] == fNow[j]:
                        fAnswer[j] = fPrev[j]

        if fPrev[4] > fNow[4]:
            for i in range(0,4):
                if fPrev[i] != fNow[i]:
                    fAnswer[i] = fPrev[i]

        if fPrev[5] < fNow[5]:
            for i in range(0,fNow[5] - fPrev[5] + 1):
                for j in range(0,4):
                    if fAnswer[j] == 0 and fPrev[j] == fNow[j]:
                        for t in range(0,4):
                            if fPrev[t] == fNow[t] and fPrev[j] != fPrev[t]:
                                fAnswer[j] = fNow[t]


print(fAnswer)
