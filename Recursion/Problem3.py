'''
Print from N to 1 using Recursion
'''

def print_number(i, n):
    if i < 1:
        return
    
    print(i)

    print_number(i - 1, n)

n = 10
print_number(10, n)