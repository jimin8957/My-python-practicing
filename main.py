def plus(a, b):
    return a+b

print(float("1.1") + float("3.5"))
print(str(5) + str(7))
age = 7
print("age = " + str(age))
year = 2022
month = 1
day = 11
today = "오늘은 {}년 {}월 {}일 입니다."
print(today.format(year, month, day))
print("오늘은 {2}일 {1}월 {0}년 입니다.".format(year, month, day))

num1 = 1
num2 = 3
print("{} 나누기 {}은 {}입니다".format(num1, num2, round(num1/num2,2)))
print("{} 나누기 {}은 {:.2f}입니다".format(num1, num2, num1/num2))
print(f"{num1} 나누기 {num2}은 {num1/num2:.2f}입니다")

wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)

print("{}시간에 {}달러 벌었습니다.".format(1, 1 * wage))
print("{}시간에 {:.1f}원 벌었습니다.".format(1, 1*wage*exchange_rate))

print(not 2<1)
print(type("3"))
print(type(plus), type(print))
