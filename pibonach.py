def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(8))

def triangle_number(n):
    if n == 1:
        return 1
    else:
        return n + triangle_number(n-1)

print(triangle_number(6))


def sum_digits(n):
    if n < 10:
        return n
    return sum_digits(n // 10) + (n % 10)

print(sum_digits(22541))
print(sum_digits(92130))



def flip(some_list):
    if len(some_list) <= 1:
        return some_list
    return some_list[-1:] + flip(some_list[:-1])

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)