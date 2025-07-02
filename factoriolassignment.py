# calculating factorial of 5


# number = n
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("Factorial of 5 is:", factorial(5))
