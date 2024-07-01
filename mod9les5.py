def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if type(result) is int:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result

sum1 = sum_three(2, 3, 6)
print(sum1)
