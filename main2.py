def print_square(x):
    print(x * x)


def get_square(x):
    return x * x


get_square(3)

print(print_square(3))


def myself(name, age, nationality = "한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("박지민", 20)  # 옵셔널 파라미터를 제공하지 않는 경우


def my_function():
    x = 3
    print(x)


my_function()


def is_evenly_divisible(num):
    return (num % 2 == 0)


print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))