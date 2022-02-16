i = 1

while i <= 100:
    if i%8 == 0 and i%12 != 0:
        print(i)
    i += 1


i = 1
sum = 0

while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        sum += i
    i += 1

print(sum)


i = 1
count = 0

while i <= 120:
    if 120 % i == 0:
        print(i)
        count += 1
    i += 1

print("120의 약수 개수 {}개".format(count))


year = 1988
money = 5000
APART = 11000

while year < 2016:
    money *= 1.12
    year += 1

if money > APART:
    print("{}원 차이로 아저씨 맞음".format(int(money-APART)))
else:
    print("{}원 차이로 아줌마 맞음".format(int(APART-money)))

num1 = 1
num2 = 1
num3 = 2
i = 1
temp = 0

while i<=50:
    print(num1)
    temp = num3
    num3 = num2 + num3
    num1 = num2
    num2 = temp
    i += 1