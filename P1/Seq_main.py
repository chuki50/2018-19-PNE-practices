from P1.Seq import Seq


s1 = Seq(input("First sequence: "))
s2 = Seq(input("Second sequence: "))

str1 = s1.strbase
str2 = s2.strbase

l1 = s1.length()
l2 = s2.length()

complement1 = s1.complementary()
reversed1 = s1.reverse()

bca1 = s1.count('A')
bcc1 = s1.count('C')
bcg1 = s1.count('G')
bct1 = s1.count('T')
bpa1 = s1.perc('A')
bpc1 = s1.perc('C')
bpg1 = s1.perc('G')
bpt1 = s1.perc('T')

bca2 = s2.count('A')
bcc2 = s2.count('C')
bcg2 = s2.count('G')
bct2 = s2.count('T')
bpa2 = s2.perc('A')
bpc2 = s2.perc('C')
bpg2 = s2.perc('G')
bpt2 = s2.perc('T')

print("Sequence 1: {}".format(str1))
print("    Length: {}".format(l1))
print("    Bases count: {}, {}, {}, {}".format(bca1, bcc1, bcg1, bct1))
print("    Bases percentage: {}, {}, {}, {}".format(bpa1, bpc1, bpg1, bpt1))

print("Sequence 2: {}".format(str2))
print("    Length: {}".format(l2))
print("    Bases count: {}, {}, {}, {}".format(bca2, bcc2, bcg2, bct2))
print("    Bases percentage: {}, {}, {}, {}".format(bpa2, bpc2, bpg2, bpt2))

print("Sequence 3: {}".format(complement1))
print("    Length: {}".format(l1))
print("    Bases count: {}, {}, {}, {}".format(bca1, bcc1, bcg1, bct1))
print("    Bases percentage: {}, {}, {}, {}".format(bpa1, bpc1, bpg1, bpt1))

print("Sequence 4: {}".format(reversed1))
print("    Length: {}".format(l1))
print("    Bases count: {}, {}, {}, {}".format(bca1, bcc1, bcg1, bct1))
print("    Bases percentage: {}, {}, {}, {}".format(bpa1, bpc1, bpg1, bpt1))


