
def main():
    file = open("./test")
    lines = file.readlines()
    slines = []
    l_box_pos = []
    circuits = []
    for line in lines:
        slines.append(line.strip())
    
    for line in slines:
        temp = line.split(",")
        temp = [int(temp[0]), int(temp[1]), int(temp[2])]
        l_box_pos.append(temp)
    

    search_list = list(l_box_pos)
    for box_pos in list(l_box_pos):
        min_dist = 1000000
        min_dist_box = []
        for cmp_box_pos in search_list: 
            dist = [abs(box_pos[0]-cmp_box_pos[0]),abs(box_pos[1]-cmp_box_pos[1]),abs(box_pos[2]-cmp_box_pos[2])]
            
            if min_dist > sum(dist): 
                min_dist = sum(dist)
                min_dist_box = cmp_box_pos
        added = False
        for circuit in circuits:

            if box_pos in circuit  and min_dist_box in circuit:
                added = True
                break
            if box_pos in circuit:
                circuits[circuits.index(circuit)].append(min_dist_box)
                added = True
                break
            if min_dist_box in circuit:
                circuits[circuits.index(circuit)].append(box_pos)
                added = True
                break
            if not added:
                circuits.append([box_pos])


    for circuit in circuits:
        print(circuit)
main()
