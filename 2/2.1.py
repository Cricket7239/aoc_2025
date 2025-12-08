
def id_is_valid(id):
    id = str(id)
    id_size = len(id)
    return id[:(id_size//2)] != id[(id_size//2):]

def sum_invalid_ids():
    infile = input()
    ranges = infile.split(",")
    sum = 0

    for n in ranges:
        start, end = n.split("-")
        for id in range(int(start), int(end)+1):
            print(f"{id}|{id_is_valid(id)}")
            if not id_is_valid(id):
                sum += id

    return sum
print(sum_invalid_ids())
