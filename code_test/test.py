import sys

# 1. 1부터 9까지의 수의 제곱 값 포함 리스트
import sys

list1 = [i*i for i in range (1, 10)]
print(list1)


# 2. N * M 크기 2차원 리스트 초기화 [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
def initialize(N, M):
    list2 = [[0] * M for _ in range (N)]
    return list2


# 3. 특정 값의 원소들만 리스트에서 제거하기
# A = [1, 2, 3, 4, 5, 5, 5] (3, 5 제거)

list3 = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

list4 = [i for i in list3 if i not in remove_set]
print(list4)


# 4. Don’t you know “Python”? 출력

print("Don't you know \"Python\"?")


# 5. 순서 없는 집합 자료형 만들기, 값 추가

set1 = set({1, 2, 3, 3, 4,})
print(set1)
set1.add(7)
set1.update([5, 6, 7, 8])
print(set1)


# 6. [90, 85, 77, 65, 97], 커트라인 80, 2, 4번 학생 탈락. for문

list5 = [90, 85, 77, 65, 97]
drop = [2, 4]

for i in range(len(list5)):
    if i + 1 in drop:
        continue
    elif list5[i] >= 80:
        print("{}번 합격".format(i + 1))


# 7. 함수로 전역 변수 바꾸기

a = 0
def change():
    global a
    a = 5
change()

print(a)


# 8. 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))


# 9. 데이터의 개수 입력 후, 문자열 띄어쓰기 구분후 각각 정수 자료형의 데이터로 저장, 역순으로 표현

n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)


# 10. n, m, k를 공백으로 구분하여 입력

n, m, k = map(int, input().split())
print(n, m, k)


# 11. input 안하고 한 줄씩 입력받기

data = sys.stdin.readline().rstrip()
print(data)


# 12. f string 쓰기

answer = 7
print(f"정답은 {answer}입니다")


