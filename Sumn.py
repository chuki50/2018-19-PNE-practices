
def sumall(a,b):
    final_result = 0
    for index in range(a,b+1):
        final_result = final_result + index
    print("The sum of all numbers from",a,"to",b,"is",final_result)

lowern = int(input("Introduce the lower boundary:"))
uppern = int(input("Introduce the upper boundary:"))
sumall(lowern,uppern)