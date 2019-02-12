class Seq1:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print("New sequence created!")

        self.strbases = strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):
    """This class is derived from the Seq. All the objects of class Gene will inherit the methods from Seq class"""
    pass


s1 = Seq1("ATTCATCC")
l1 = s1.len()
s2 = Seq1("AAACTTGG")
l2 = s2.len()

str1 = s1.strbases
str2 = s2.strbases

print("Sequence 1: {}".format(str1))
print("    Length: {}".format(l1))

print("Sequence 2: {}".format(str2))
print("    Length: {}".format(l2))

print("The End?")
