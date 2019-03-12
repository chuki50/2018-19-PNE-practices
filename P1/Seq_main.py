# First, we need to import our class from the other file.
from P1.Seq import Seq


# Now, we let the user introduce the 2 sequences, and we introduce them to the Seq class.
# We are only going to accept the bases A C G and T.
s1 = input("First sequence: ").upper()
for i in range(len(s1)):
    while s1[i] not in ['A', 'C', 'G', 'T']:
        s1 = input("Sorry, one base isn't valid. Introduce the first sequence again: ")

s2 = input("Second sequence: ").upper()
for i in range(len(s2.upper())):
    while s2[i] not in ['A', 'C', 'G', 'T']:
        s2 = input("Sorry, one base isn't valid. Introduce the second sequence again: ")

s1 = Seq(s1)
s2 = Seq(s2)


# Now we can make them strings
str1 = s1.strbase
str2 = s2.strbase
# And calculate their length with the method defined inside the seq class.
# We can do the complementary and reversed sequence of the first one as well.
l1 = s1.length()
l2 = s2.length()

complement1 = s1.complementary()
reversed1 = s1.reverse()

# We use the count and perc methods to count all the bases and calculate their percentage inside a sequence.
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

# Now we print the information calculated.
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


