# Factorial of larger number

def factorial (n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
def factorial_of_larger_number(n):
    return list(str(factorial(n)))

n = 5
print(factorial_of_larger_number(n))