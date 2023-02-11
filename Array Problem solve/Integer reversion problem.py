'''
reversed=0
remainder=0
n=1234
while(n>0):
        remainder=n%10
        n=n/10
        reversed=reversed*10+remainder
'''
def reversed_number(n):
    remainder = 0
    reversed = 0
    while n > 0:
        remainder = n % 10
        n = n // 10
        reversed = reversed * 10 + remainder
    return reversed

if __name__=='__main__':
    n = 823
    print(reversed_number(n))

