'''
Print 1 to N using recursion
'''

def print_number(i, n):
    if i > n:
        return
    
    print(i)

    print_number(i + 1, n)


n = 10
print_number(1, n)