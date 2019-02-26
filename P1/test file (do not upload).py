def count(seq, base):
    counter = 0
    for strbase in range(len(seq.strbase)):
        if strbase == base:
            counter += 1
    return base, counter


count("AGCTCTACTCT","T")
print("")