'''
check if a string is Palindrome or not
'''

def palindrome(i, s):
    if(i >= len(s)/2):
        return True
    
    if(s[i] != s[len(s) - i - 1]):
        return False
    
    return palindrome(i + 1, s)

s = "ABCDCBA"
print(palindrome(0, s))