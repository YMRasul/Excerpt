from mkofile import *
from clr import clear_screen
from spr011 import readspr

if __name__ == '__main__':

    clear_screen()

    spr = '011'
    print(f"{spr=}")

    file_path1 = './in/smko.txt'
    print("Открываем", file_path1)
    txt = firead(file_path1,spr)

    file_path2 = './tmp/'+spr+'.txt'
    print("Записываем", file_path2)
    txtwrite(file_path2,txt)

    #---------------------------------------------
    spr = input("Введите код справочника:")
    print(f"{spr=}")
    if spr != '011':
        file_path1 = './in/smko.txt'
        print("Открываем", file_path1)
        txt = firead(file_path1,spr)

        file_path2 = './tmp/'+spr+'.txt'
        print("Записываем", file_path2)
        txtwrite(file_path2,txt)

        # По справочнику 011 определяем столбцы
        # и считываем справочника spr

        tx = readspr(spr)
        file_path2 = './out/' + spr + '.txt'
        print("Записываем", file_path2)
        txtwrite(file_path2,tx)

        print('Готова !!!')
    else:
        print(f"{spr=} Это описатель справочников!")
