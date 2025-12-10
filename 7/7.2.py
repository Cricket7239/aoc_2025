
counter = 1

def right(slines):
    for j in range(0, len(slines[0])):
        list_sline = list(slines[1])
        if slines[1-1][j] == '|' and slines[1][j] == '^':
            list_sline[j+1] = '|'
            slines[1] = ''.join(list_sline)
            global counter
            counter +=1
        
        if slines[1-1][j] == '|' and slines[1][j] == '.':
            list_sline[j] = '|'
            slines[1] = ''.join(list_sline)
    if len(slines) ==2 : return
    left(list(slines[1:]))
def left(slines):
    for j in range(0, len(slines[0])):
        list_sline = list(slines[1])
        if slines[1-1][j] == '|' and slines[1][j] == '^':
            list_sline[j-1] = '|'
            slines[1] =''.join(list_sline)
            global counter
            counter += 1
        
        if slines[1-1][j] == '|' and slines[1][j] == '.':
            list_sline[j] = '|'
            slines[1] = ''.join(list_sline)
    if len(slines) ==2 : return
    right(list(slines))
def main():
    file = open("./test","r")
    lines = file.readlines()
    slines = []
    for line in lines:
        slines.append(line.strip('\n'))
    left(slines)

    for line in slines:
        print(line)
    print(counter)
main()
