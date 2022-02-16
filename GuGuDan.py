i = 1

while i <= 9:
    j = 1
    while j<=9:
        print("{} * {} = {}".format(i, j, i*j))
        j += 1
    i += 1

numbers = [2, 3, 5, 7, 11, 13]
print(numbers[0:4])
print(numbers[2:])

numbers.insert(4, 37)
print(numbers)


number = []
number.append(5)
number.append(8)

print(number)
print(len(number))

del number[0]

print(number)


chaos = [19, 13, 2, 5, 3, 11, 17, 7]
print(sorted(chaos))
print(sorted(chaos, reverse=True))
chaos.sort()
print(chaos)
chaos.sort(reverse=True)
print(chaos)

greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
i = 0
while i < len(greetings):
    print(greetings[i])
    i += 1


# Flist = [40, 15, 32, 64, -4, 11]
# C = []
#
# #/def fah_to_cel(F):
#     i=0
#     while i < len(F):
#         C.append(((F[i]-32)*5)/9)
#     print(C)
#
# fah_to_cel(Flist)

Flist = [40, 15, 32, 64, -4, 11]
i = 0

def fah_to_cel(F):
    return (F - 32) * 5 / 9

while i < len(Flist):
    Flist[i] = round(fah_to_cel(Flist[i]), 1)
    i += 1

print("섭씨 온도 리스트: {}".format(Flist))


def ko_to_us(K):
    return K / 1000


def us_to_jp(U):
    return U * 125


# i = 0
# ko = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
# us = []
# jp = []
#
#
# while i < len(ko):
#     us[i] = ko_to_us(ko[i])
#     jp[i] = us_to_jp(us[i])
#     i += 1
#
# print("{} {}".format(us, jp))


i = 0
ko = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]

print("한국돈은 " + str(ko))

while i < len(ko):
    ko[i] = ko_to_us(ko[i])
    i += 1

print("미국돈은 {}".format(ko))

i = 0

while i < len(ko):
    ko[i] = us_to_jp(ko[i])
    i += 1

print("일본돈은 {}".format(ko))


numbers = [1, 7, 3, 6, 5, 2, 13, 14]
print(numbers)

i=0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:
        i += 1

print(numbers)

numbers.insert(0, 20)

print(numbers)

numbers.sort()

print(numbers)
