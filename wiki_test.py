def pressure(string):
    start = 0
    result = ""

    while start < len(string) - 1:
        count = 1
        while string[start] == string[start + 1]:
            count += 1
            start += 1
            if start == len(string) - 2:
                if string[-1] == string[start]:
                    count += 1
                else:
                    count = str(count) + string[-1] + "1"
        result += string[start] + str(count)
        start += 1
    return result

print(pressure("aaabbcccccca"))

def compress_string(s):
    _alpha = ""
    cnt = 0
    result = ""
    for alpha in s:
        if alpha!=_alpha:
            _alpha = alpha
            if cnt: result += str(cnt)
            result += alpha
            cnt = 1
        else:
            cnt +=1
    if cnt: result += str(cnt)
    return result

print(compress_string("aaabbcccccca"))  # a3b2c6a1 출력

def Duplicate_numbers(number):
    num = str(number)
    if '0' in num and '1' in num and '2' in num and '3' in num and '4' in num and '5' in num and '6' in num and '7' in num and '8' in num and '9' in num:
        return True
    else:
        return False


def DashInsert(numbers):
    result = []
    numberss = []
    for num in str(numbers):
        numberss.append(num)
    for i in range(len(numberss) - 1):
        result.append(numberss[i])
        if int(numberss[i]) % 2 == 0 and int(numberss[i + 1]) % 2 == 0:
            result.append('*')
        elif int(numberss[i]) % 2 == 1 and int(numberss[i + 1]) % 2 == 1:
            result.append('-')
        else:
            pass
    result.append(numberss[-1])
    return result

print("".join(DashInsert(4546793)))


class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        sum = 0
        for num in self.numbers:
            sum += int(num)
        print(sum)

    def avg(self):
        sum = 0
        for num in self.numbers:
            sum += int(num)
        print(sum / len(self.numbers))

cal1 = Calculator([1, 2, 3, 4, 5])
cal1.sum()  # 합계
cal1.avg()  # 평균

cal2 = Calculator([6, 7, 8, 9, 10])
cal2.sum()  # 합계
cal2.avg()  # 평균