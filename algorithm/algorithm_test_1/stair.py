# 1번 문제
# def staircase(n):
#     i = 1
#     j = 1
#     for k in range(n):
#         i, j = j, i + j
#     return i

# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    i = 1
    for step in possible_steps:


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))