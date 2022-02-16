a = 'a:b:c:d'
b = a.split(':')
print('#'.join(b))

a = {'A':90, 'B':80}
print(a.get('C', 70))

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in range(len(A)):
    if A[i] >= 50:
        sum += A[i]
print(sum)

def pivo(n):
    a = 0
    b = 1
    c = 1
    result = []
    while n > a:
        result.append(a)
        temp = b
        a = b
        b = c
        c = temp + c
    return result

print(pivo(15))


def sumsum(k):
    kk = k.split(",")
    sum = 0
    for i in range(len(kk)):
        sum += int(kk[i])
    return sum

print(sumsum('65,45,2,3,45,8'))


a = input("구구단 출력할 숫자 입력: ")
for i in range(1, 10):
    print(i * int(a), end=' ')
print('\n')

with open('abc.txt', 'r') as f:
    app = []
    for line in f:
        app.append(line.strip())

with open('abc.txt', 'w') as f:
    for i in range(len(app)):
        f.write(app[len(app) - i - 1] + '\n')


with open('sample.txt', 'r') as f:
    app = []
    for line in f:
        app.append(line.strip())

sum = 0
for i in range(len(app)):
    sum += int(app[i])
avg = sum / len(app)

f = open("result.txt", "w")
f.write(str(avg) + '\n')
f.write(str(sum))
f.close()


class calculator:
    def __init__(self, list):
        self.list = list

    def sum(self):
        sum = 0
        for num in self.list:
            sum += num
        return sum

    def avg(self):
        sum = 0
        for num in self.list:
            sum += num
        return sum / len(self.list)

cal1 = calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())
cal2 = calculator([6,7,8,9,10])
print(cal2.sum())
