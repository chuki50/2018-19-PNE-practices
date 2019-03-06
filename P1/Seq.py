def countbases(sequence, base):
    counter = 0
    for x in range(len(sequence)):
        if sequence[x] == base:
                counter += 1
    return counter


class Seq:
    # We are going to use this class for the sequences of DNA.
    # 1. Class initialization.
    def __init__(self, strbase):
        print("New sequence created!")

        self.strbase = strbase

    # 2. Length of the sequence.
    def length(self):
        return len(self.strbase)

    # 3. Complementary sequence, following the pairs C <-> G and T <-> A.
    def complementary(self):
        notcompl = str(self.strbase)
        compl = ''
        for i in range(len(notcompl)):
            if notcompl[i] == 'A':
                    compl = compl + 'T'
            elif notcompl[i] == 'T':
                    compl = compl + 'A'
            elif notcompl[i] == 'C':
                    compl = compl + 'G'
            elif notcompl[i] == 'G':
                    compl = compl + 'C'
        return compl

    # 4. Reverse sequence.
    def reverse(self):
        reverse_seq = self.strbase[::-1]
        return reverse_seq

    # 5. Base counter
    def count(self, base):
        counter = 0
        for x in range(len(self.strbase)):
            if self.strbase[x] == base:
                counter += 1
        bcount = str("{}:{}".format(base, counter))
        return bcount

    # 6. Base percentage
    def perc(self, base):
        percentage = round(100.0 * countbases(self.strbase, base) / len(self.strbase))
        bperc = str("{}:{}%".format(base, percentage))
        return bperc