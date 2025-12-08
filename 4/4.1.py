
def main():
    file = open("./input", "r")
    layers = file.readlines()
    out = 0
    for i in range(0,len(layers)):
        layers[i] = layers[i].strip("\n") 
    layers.append(" "*len(layers[0]))

    removed = 1
    while removed:
        removed = 0
        for i in range(0, len(layers)-1):
            for j in range(0, len(layers[i])):
                uper_line = layers[i-1][j-1:j] + layers[i-1][j:j+2]
                line = layers[i][j-1:j] + layers[i][j+1:j+2]
                lower_line = layers[i+1][j-1:j] + layers[i+1][j:j+2] 
                if layers[i][j] == "@":
                    x = uper_line.count('@')
                    y = line.count('@')
                    z = lower_line.count('@')
                    if x+y+z < 4:
                        temp = list(layers[i])
                        temp[j] = '.'
                        layers[i] = "".join(temp)
                        out += 1 
                        removed += 1
    print(out)
main()
