import json
import termcolor

f = open("person", 'r')
person = json.load(f)
f.close()

f = open("person2", 'r')
person2 = json.load(f)
f.close()

f = open("person3", 'r')
person3 = json.load(f)
f.close()

people = [person, person2, person3]
for x in people:
    termcolor.cprint("Name: ",'cyan',end='')
    print(x['Firstname'], x['Lastname'])
    termcolor.cprint("Age: ",'cyan',end='')
    print(x['Age'])
    for i, num in enumerate(x['phoneNumber']):
        termcolor.cprint("Phone {}".format(i), 'cyan',)
        termcolor.cprint("     Type: ", 'blue', end='')
        print(num['type'])
        termcolor.cprint("     Num: ", 'blue', end='')
        print(num['number'])
    print("")


