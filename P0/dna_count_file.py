def dna_count(file):
    dna = ""
    with open(file, 'r') as f:
        for line in f:
            line = line.strip("\n")
            line = line.strip(" ")
            dna = dna + line

    a_count = 0
    g_count = 0
    c_count = 0
    t_count = 0
    valid = True
    error_places = []
    for x in range(len(dna)):
        if dna[x] not in ["A", "G", "C", "T"]:
            error_places.append(x)
            valid = False
        elif dna[x] == "A":
            a_count += 1
        elif dna[x] == "G":
            g_count += 1
        elif dna[x] == "C":
            c_count += 1
        elif dna[x] == "T":
            t_count += 1

    if valid:
        print("The number of bases in your sequence are: \nA:", a_count, "\nG:", g_count, "\nC:", c_count, "\nT:",
              t_count)
    else:
        print("One or more bases are invalid. Check your base at:", error_places)


dna_count("dna.txt")
