
def sum_packs():
    datei = open("./input", "r")
    packs = datei.readlines()
    out = 0
    for pack in packs:
        pack = pack.strip()
        stack = []
        to_remove = len(pack) -12
        for d in pack:
            while to_remove and stack and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)

        if to_remove:
            stack = stack[:-to_remove]
        out += int(''.join(stack))
    print(out)
sum_packs()
