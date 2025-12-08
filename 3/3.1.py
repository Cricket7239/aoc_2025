
def sum_packs():
    datei = open("./input", "r")
    packs = datei.readlines()
    out = 0
    for pack in packs:
        pack = pack.strip()
        jults = ""
        x = max(pack[:-1])
        y = max(pack[pack.index(x)+1:])
        jults = x + y
        out += int(jults)
    print(out)
sum_packs()
