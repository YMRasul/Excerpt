def  read011(kodspr):
    pole = []

    path = './tmp/011.txt'
    print("Открываем", path)
    kod = "011" + kodspr
    txt = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith(kod):
                txt.append(line)

    ln = len(txt)
    if ln > 0:
        for i in range(ln):
            s = txt[i]
            p0 = s[0:3]  # Код самого справочника
            p1 = s[3:6]  # Код справочника

            p2 = int(s[6:8]) # Код поле
            p3 = s[8:88]     # Наименование поле

            p4 = int(s[88:91]) #  Длина поле
            p5 = int(s[91:95]) #  Начиная с позиции
            p6 = int(s[95:99]) #  кол-во символов

            p7 = s[99:100]     # 'B' 'K'

            #print(f"{ln=} {p0=} {p1=} {p2=} {p3=} {p4=} {p5=} {p6=} {p7=}")
            pole.append([p2,p3,p4,p5,p6,p7])
    return pole
#----------------------------------
def readspr(spr):
    pole = read011(spr)  # Данные справочника spr
    kol = len(pole)
    txt = []

    sl = ''.ljust(pole[kol-1][4] + kol,'-') +'\n'


    s = ''
    for i in range(kol):
        st = f"{pole[i][0]} {pole[i][1]} {pole[i][2]} ({pole[i][3]},{pole[i][4]} {pole[i][5]})"
        txt.append(st + '\n')
        s = s +  str(pole[i][0]).center(pole[i][2]) + '|'

    #print(s)
    txt.append(sl)            #
    txt.append(s + '\n')    #  Шапка таблицы
    txt.append(sl)            #


    file = './tmp/'+spr+'.txt'
    #print("Открываем", file)
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            #print(line)
            s = ''
            for i in range(kol):

                s = s + line[pole[i][3]-1:pole[i][4]] + ' '
            #print(s)
            txt.append(s+'\n')
    return txt




