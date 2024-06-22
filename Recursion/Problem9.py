'''
Print from 1 to N using backtracking
(can't use i + 1)
'''

def print_number(i, n):
    if (i < 1):
        return
    
    print_number(i - 1, n)

    print(i)

n = 10
print_number(n, n)