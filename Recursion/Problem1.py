'''
Print your name N times
'''

def print_name(i,n):

    if ( i == n):
        return

    print("Naresh")

    print_name(i + 1, n)

n = 5
print_name(0, n)