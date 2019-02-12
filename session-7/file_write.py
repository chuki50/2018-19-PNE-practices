myfile = open(NAME,'r')

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("Contents are: {}".format(contents))

myfile.close()

