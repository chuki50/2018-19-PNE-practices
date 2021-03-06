#Count the number of bases in a DNA sequence. The sequence is input by the user
def dnacount(sequence):
    dna = sequence.upper()
    a_count = 0
    g_count = 0
    c_count = 0
    t_count = 0
    valid = True
    for x in range(len(dna)):
        if dna[x] not in ["A","G","C","T"]:
            error_place = x+1
            valid = False
            break
        elif dna[x] == "A":
            a_count += 1
        elif dna[x] == "G":
            g_count += 1
        elif dna[x] == "C":
            c_count += 1
        elif dna[x] == "T":
            t_count += 1
    if valid == True:
        print("The number of bases in your sequence are: \nA:", a_count,"\nG:", g_count,"\nC:", c_count,"\nT:", t_count)
    else:
        print("One or more bases are invalid. Check your base at",error_place)

dnacount("AGGGTTSTTCC")