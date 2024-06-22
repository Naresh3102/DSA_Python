'''
Print Fibonacci series up to Nth term
'''

def fibonacci(n):

    if (n == 0):
        return 0

    if (n <= 1):
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci(n):
    for i in range(n+1):
        print(fibonacci(i), end=" ")

n = 5
print_fibonacci(n)