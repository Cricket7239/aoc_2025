datei = open("./rotaitions", "r")
lines = datei.readlines()


def count_zero_hits(lines, start=50):
    pos = start
    hits = 0
    dial_size=100

    for line in lines:
        line = line.strip()
        richtung = line[0]
        wert = int(line[1:])

        start_at_zero = pos == 0

        abstand = (dial_size - pos) % dial_size if richtung == "R" else pos % dial_size
        if abstand == 0 or start_at_zero:
            abstand = dial_size

        if abstand <= wert:
            hits += 1 + (wert - abstand) 

        pos = (pos + wert) % dial_size if richtung == "R" else (pos - wert) % dial_size

        if pos == 0 and (wert % dial_size) != abstand:
            hits += 1

    return hits

print(f"Total zero hits: {count_zero_hits(lines)}")

