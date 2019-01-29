# Adding the numbers from 1 to n, where n is a parameter defined in the code.
# It should be implemented by calling a function that perform the addition of the n first integers numbers (1+2+3+...+n)
def sum_n(n):
    result = 0
    for i in range(n):
        result = result + (i + 1)

    print("The result of adding all the numbers from 1 to", n, "is", result)


sum_n(int(input("Introduce the upper bound:")))
