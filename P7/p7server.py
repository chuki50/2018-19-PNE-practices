import http.client
import json
import termcolor


# We are going to be connecting to the ENSEMBL project server, under the category of sequence/id.
SERVER = 'rest.ensembl.org'

print("\nConnecting to server: {}\n".format(SERVER))
conn = http.client.HTTPConnection(SERVER)

# Now we use the GET resource to make the request. The FRAT1 gene is ENSG00000165879 in ENSMBL

conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

# Read the response message from the server
r = conn.getresponse()

print("Response received!: {} {}\n".format(r.status, r.reason))

# We are going to transfer the response into a json format, and we are going to work on the sequence from there on.
data = r.read().decode("utf-8")
information = json.loads(data)

# Our parameters are 'seq','query','desc','molecule','id' and 'version', in that order. We'll only use the first one.
main_sequence = information['seq']

# Now we are going to be answering the questions:
    #1.- How many bases are there in the FRAT1 gene?
    #2.- How many T bases are there in the FRAT1 gene?
    #3.- Which base is the most popular in the FRAT1 gene? What is its percentage?
    #4.- Calculate the percentage of all the bases in the FRAT1 gene

num_bases = len(main_sequence)

counterA = 0
counterC = 0
counterG = 0
counterT = 0

for x in range(len(main_sequence)):
    if main_sequence[x] == "A":
        counterA += 1
    elif main_sequence[x] == "C":
        counterC += 1
    elif main_sequence[x] == "G":
        counterG += 1
    elif main_sequence[x] == "T":
        counterT += 1
counter_list = [counterA, counterC, counterG, counterT]
popular_base = max(counter_list)

percA = round(100 * counterA / num_bases)
percC = round(100 * counterC / num_bases)
percG = round(100 * counterG / num_bases)
percT = round(100 * counterT / num_bases)

popular_perc = float()
base = str()

if popular_base == counterA:
    popular_perc = percA
    base = 'A'
elif popular_base == counterC:
    popular_perc = percC
    base = 'C'
elif popular_base == counterG:
    popular_perc = percG
    base = 'G'
elif popular_base == counterT:
    popular_perc = percT
    base = 'T'

termcolor.cprint('FRAT1 gene:', 'cyan')
print(' Number of bases in the FRAT1 gene: {}'.format(num_bases))
print(' Number of T bases: {}'.format(counterT))
print(' Most popular base: {} with {} bases ({}%)'.format(base, popular_base, popular_perc))
print(' Percentages of bases:')
print('     A: {}%'.format(percA))
print('     C: {}%'.format(percC))
print('     G: {}%'.format(percG))
print('     T: {}%'.format(percT))












