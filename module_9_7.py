def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if isinstance(result, int):
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    s_m = a + b + c
    return s_m


result = sum_three(2, 3, 6)
print(result)
