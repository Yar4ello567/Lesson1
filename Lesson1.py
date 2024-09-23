import math

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

with open('in_nums.txt', 'r') as in_file, open('out_nums.txt', 'w') as out_file:
    for line in in_file:
        number = int(line.strip())
        if number > 1 and all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1)):
            last_digit = number % 10
            fibonacci_number = fib(last_digit)
            out_file.write(str(fibonacci_number) + '\n')