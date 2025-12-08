datei = open("./rotaitions", "r")
lines = datei.readlines()

counter = 0
pos = 50

def rotate():
    
    global pos
    for line in lines:
        if(line.startswith("R")):
            pos += int(line[1:-1])
            if pos > 99: pos = pos % 100
        else:
            pos -= int(line[1:-1])
            if pos < 0: pos = 100 - (abs(pos) % 100)
            if pos == 100: pos = 0
        
        if not pos:
            global counter
            counter += 1
rotate()
print(f"[{counter}]")
