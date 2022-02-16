import random


def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        num = random.randint(0, 9)
        if num not in numbers:
            numbers.append(num)
    return numbers


def take_guess():
    guess = []
    print("숫자 3개 한개씩 입력")
    a = int(input("첫 숫자 입력: "))
    while a < 0 or a > 9:
        print("범위에 벗어나는 숫자. 다시 입력")
        a = int(input("첫 숫자 입력: "))
    guess.append(a)
    b = int(input("둘 숫자 입력: "))
    while b < 0 or b > 9:
        print("범위에 벗어나는 숫자. 다시 입력")
        b = int(input("둘 숫자 입력: "))
    while b in guess:
        print("중복되는 숫자. 다시 입력")
        b = int(input("둘 숫자 입력: "))
    guess.append(b)
    c = int(input("셋 숫자 입력: "))
    while c < 0 or c > 9:
        print("범위에 벗어나는 숫자. 다시 입력")
        c = int(input("셋 숫자 입력: "))
    while c in guess:
        print("중복되는 숫자. 다시 입력")
        c = int(input("셋 숫자 입력: "))
    guess.append(c)
    return guess


def get_score(guess, solution):
    strike = 0
    ball = 0
    for i in range(3):
        for j in range(3):
            if guess[i] != solution[i] and guess[i] == solution[j]:
                ball += 1
        if guess[i] == solution[i]:
            strike += 1
    return strike, ball

strike = 0
count = 0
answer = generate_numbers()
while strike != 3:
    print(answer)
    strike, ball = get_score(take_guess(), answer)
    print("{}S {}B".format(strike, ball))
    count += 1
print("축하합니다. {}만에 맞췄습니다.".format(count))
