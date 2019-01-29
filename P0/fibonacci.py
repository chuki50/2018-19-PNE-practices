#It prints the first n terms of the fibonacci series. The n parameter is a constant inside de code
def fibonacci(n):
    fibonacci_sequence = [1,1]
    for i in range(n-2):
        fibonacci_sequence.append((fibonacci_sequence[i+1]+fibonacci_sequence[i]))
    print(fibonacci_sequence)


fibonacci(int(input("Introduce the number of items for your Fibonacci sequence:")))