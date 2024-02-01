def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("Input 'n' must be greater or equal to 0 !!!")
    elif n > 12:
        raise ValueError("Input 'n' must be less or equal to 12 !!!")
    else:
        return n*factorial(n-1)
    

print(factorial(12))
