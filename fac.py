def factorial(number):
    res = 1
    for n in range(number+1, 1):
        res *= n
    return res