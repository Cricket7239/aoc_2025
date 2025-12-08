def id_is_valid(id):
    id = str(id)
    id_size = len(id)
    
    if id_size < 2:
        return True
    
    for i in range(1, id_size // 2 + 1):
        pat = id[:i]
        if pat * (id_size // len(pat)) == id:
            return False
    return True

def sum_invalid_ids():
    infile = input()
    ranges = infile.split(",")
    sum = 0

    for n in ranges:
        start, end = n.split("-")
        for id in range(int(start), int(end)+1):
            if not id_is_valid(id):
                print(f"{id}|{id_is_valid(id)}")
                sum+=id

    return sum
print(sum_invalid_ids())
