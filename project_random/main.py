from char import *

char1_name = input("1p 이름을 입력하세요: ")
char1_job = input("직업을 선택하세요 1. gambler 2. tank ")
if char1_job == str(1):
    char1 = gamble(char1_name)
elif char1_job == str(2):
    char1 = tank(char1_name)


char2_name = input("2p 이름을 입력하세요: ")
char2_job = input("직업을 선택하세요 1. gambler 2. tank ")
if char2_job == str(1):
    char2 = gamble(char2_name)
elif char2_job == str(2):
    char2 = tank(char2_name)


while char1.health > 0 and char2.health > 0:
    decision1 = input(f"{char1}, 무슨 행동을 할 것인가요?")
    if decision1 == str(1):
        char1.sk_1()
    elif decision1 == str(2):
        char1.sk_2()
    elif decision1 == str(3):
        char1.sk_3()
    elif decision1 == str(4):
        char1.sk_4()
    elif decision1 == 's':
        char1.special()

    decision2 = input(f"{char2}, 무슨 행동을 할 것인가요?")
    if decision1 == str(1):
        char2.sk_1()
    elif decision1 == str(2):
        char2.sk_2()
    elif decision1 == str(3):
        char2.sk_3()
    elif decision1 == str(4):
        char2.sk_4()
    elif decision1 == 's':
        char2.special()

    char1.health += char1.heal
    char2.health += char2.heal
    char1.health -= char2.damage
    char2.health -= char1.damage

    char1.damage = 0
    char1.heal = 0
    char2.damage = 0
    char2.heal = 0


    print(f"{char1_name}의 체력은 {char1.health}, {char2_name}의 체력은 {char2.health}입니다")

if char1.health <= 0 and char2.health <= 0:
    print("비겼습니다")
elif char1.health <= 0 and char2.health > 0:
    print(f"{char2_name}의 승리입니다!")
else:
    print(f"{char1_name}의 승리입니다!")