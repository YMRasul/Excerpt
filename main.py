from mkofile import *
from clr import clear_screen

if __name__ == '__main__':

    clear_screen()

    spr = input("введите код справочника:")

    print(f"{spr=}")

    file_path1 = './in/smko.txt'
    print("Открываем", file_path1)
    txt = firead(file_path1,spr)

    file_path2 = './tmp/'+spr+'.txt'
    print("Записываем", file_path2)
    txtwrite(file_path2,txt)
    print('Готова !!!')
