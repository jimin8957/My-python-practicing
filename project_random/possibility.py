import random

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def ninety():
    random_num = []
    while len(random_num) < 9:
        number = random.randint(0,9)
        if number not in random_num:
            random_num.append(number)
    new_num = random.randint(0, 9)
    if new_num in random_num:
        return True
    else:
        return False

def seventy():
    random_num = []
    while len(random_num) < 7:
        number = random.randint(0,9)
        if number not in random_num:
            random_num.append(number)
    new_num = random.randint(0, 9)
    if new_num in random_num:
        return True
    else:
        return False

def fifty():
    random_num = []
    while len(random_num) < 5:
        number = random.randint(0,9)
        if number not in random_num:
            random_num.append(number)
    new_num = random.randint(0, 9)
    if new_num in random_num:
        return True
    else:
        return False

def forty():
    random_num = []
    while len(random_num) < 4:
        number = random.randint(0,9)
        if number not in random_num:
            random_num.append(number)
    new_num = random.randint(0, 9)
    if new_num in random_num:
        return True
    else:
        return False

def thirty():
    random_num = []
    while len(random_num) < 3:
        number = random.randint(0,9)
        if number not in random_num:
            random_num.append(number)
    new_num = random.randint(0, 9)
    if new_num in random_num:
        return True
    else:
        return False

def fifteen():
    random_num = []
    while len(random_num) < 3:
        number = random.randint(0,9)
        if number not in random_num:
            random_num.append(number)
    new_num = random.randint(0, 9)
    if new_num in random_num:
        first = True
    else:
        first = False
    if random.randint(0, 9) > 4:
        second = True
    else:
        second = False
    if first == True and second == True:
        return True
    else:
        return False

def ten():
    random_num = []
    while len(random_num) < 1:
        number = random.randint(0,9)
        if number not in random_num:
            random_num.append(number)
    new_num = random.randint(0, 9)
    if new_num in random_num:
        return True
    else:
        return False

