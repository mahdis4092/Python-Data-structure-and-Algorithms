'''
Input  : n = 2
Output : 1

Input  : n = 9
Output : 34
'''

# Fibonacci Series using Dynamic Programming
def fibonacci(n):
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


print(fibonacci(9))

#repeated recursion solution
# Fibonacci series using recursion
'''
def fibonacci(n):
	if n <= 1:
		return n
	return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
	n = 9
	print(fibonacci(n))

# This code is contributed by Manan Tyagi.
'''