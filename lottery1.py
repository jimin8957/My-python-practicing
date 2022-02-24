def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        num = random.randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers


def drawing_winning_numbers():
    number = []
    numbers = generate_numbers(7)
    number = sorted(numbers[:6])
    number.append(numbers[6])
    return number


def count_matching_numbers(a, b):
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                count += 1
    return count


def check(a, b):
    special = b[6]
    b = b[:6]
    if count_matching_numbers(a, b) == 3:
        print(5000)
    elif count_matching_numbers(a, b) == 4:
        print(50000)
    elif count_matching_numbers(a, b) == 5 and special in a:
        print("5천만")
    elif count_matching_numbers(a, b) == 5:
        print("1백만")
    elif count_matching_numbers(a, b) == 6:
        print("10억")
    else:
        print("꽝")


print(generate_numbers(6))
print(drawing_winning_numbers())
print(count_matching_numbers(generate_numbers(6), generate_numbers(6)))
check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25])
