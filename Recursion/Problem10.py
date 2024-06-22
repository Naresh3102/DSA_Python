'''
Print from N to 1 using backtracking
'''

def print_number(i, n):
    if i > n:
        return
    
    print_number(i + 1, n)

    print(i)

n = 10
print_number(1, n)