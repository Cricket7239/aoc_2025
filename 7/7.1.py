
def main():
    file = open("./input", "r")
    lines = file.readlines()[1:]
    slines = []
    counter = 0
    for line in lines:
        slines.append(line.strip('\n'))
    for i in range(0, len(slines)):
        for j in range(0, len(slines[i])):
            list_sline = list(slines[i])
            if slines[i-1][j] == '|' and slines[i][j] == '^':
                list_sline[j-1] = '|'
                list_sline[j+1] = '|'
                slines[i] = ''.join(list_sline)
            
            if slines[i-1][j] == '|' and slines[i][j] == '.':
                list_sline[j] = '|'
                slines[i] = ''.join(list_sline)

    
    for i in range(0, len(slines)):
        for j in range(0, len(slines[i])):
            list_sline = list(slines[i])
            if slines[i-1][j] == '|' and slines[i][j] == '^':
                counter += 1
    for line in slines:
        print(line)
    print(counter)
main()
