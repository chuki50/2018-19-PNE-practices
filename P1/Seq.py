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
        notcompl = str(self)
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
        reverse_sequence = str(self[::-1])
        return reverse_sequence

    # 5. Base counter
    def count(self, base):
        counter = 0
        for strbase in range(len(self.strbase)):
            if strbase == base:
                counter += 1
        return base, counter

    # 6. Base percentage
    def perc(self, base):
        percentage = round(100.0 * count(self, base) / len(self.strbase))
        return base, percentage


s1 = Seq(input("Introduce the sequence: "))
l1 = s1.length()
compl1 = s1.complementary()
bc1 = s1.count('A'), s1.count('C'), s1.count('G'), s1.count('T')
str1 = s1.strbase

print("Sequence 1: {}".format(str1))
print("    Length: {}".format(l1))
print("    Bases count: {}".format(bc1))
