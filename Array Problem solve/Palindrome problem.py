#Solution-1
def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False

s='madam'
print(palindrome(s))

