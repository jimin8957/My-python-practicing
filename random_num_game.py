import random

qus = int(random.randint(1, 20))

for i in range(4):
    print("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(4-i))
    ans = int(input(""))
    if ans == qus:
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(i+1))
        break
    else:
        if ans > qus:
            print("Down")
        else:
            print("Up")
    if i == 3:
        print("아쉽습니다 정답은 {}입니다".format(qus))