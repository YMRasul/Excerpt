def  firead(path,kod):
    txt = []
    with open(path, 'r', encoding='cp866') as file:
        for line in file:
            if line.startswith(kod):
                txt.append(line)
    return txt
#--------------------------------------------
def txtwrite(path,txt):
    e = 1
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(txt)
    return e
