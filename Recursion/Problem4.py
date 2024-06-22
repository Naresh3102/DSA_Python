'''
Sum of first N Natural Numbers
'''

def natural_sum(sum, n):
    if n < 1:
        print(sum)
        return
    
    sum += n

    natural_sum(sum, n - 1)

n = 5
natural_sum(0, n)