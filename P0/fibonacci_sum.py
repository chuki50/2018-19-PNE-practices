#Adding the fibonacci terms from 1 to n. The n parameter should be enter by the user
def sum_fibonacci(n):
    n = int(n)
    sum_result = 0
    fibonacci_sequence = [1, 1]
    if n == 1:
        sum_result = 1
    elif n == 0:
        print("The number has to be greater than 1.")
    else:
        for i in range(n - 2):
          fibonacci_sequence.append(int((fibonacci_sequence[i + 1] + fibonacci_sequence[i])))
        for x in range(len(fibonacci_sequence)):
          sum_result = sum_result + int(fibonacci_sequence[x])



    print("The result of adding the terms of the Fibonacci Sequence from 1 to", n,"is",sum_result)


sum_fibonacci(input("Introduce the upper bound to sum the numbers of a Fibonacci Sequence: "))
