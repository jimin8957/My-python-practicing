# 1번 문제
# def sublist_max(profits):
#     max_p = profits[0]
#     for i in range(len(profits)):
#         result = 0
#         for j in range(i, len(profits)):
#             result += profits[j]
#             max_p = max(result, max_p)
#     return max_p


#2번 문제
# def max_crossing_sum(profits, start, end):
#     mid = (start + end) // 2
#
#     left_sum = 0
#     left_max = profits[mid]
#
#     for i in range(mid, start - 1, -1):
#         left_sum += profits[i]
#         left_max = max(left_max, left_sum)
#
#     right_sum = 0
#     right_max = profits[mid + 1]
#
#     for i in range(mid + 1, end + 1):
#         right_sum += profits[i]
#         right_max = max(right_max, right_sum)
#
#     return left_max + right_max
#
#
# def sublist_max(profits, start, end):
#     mid = (start + end) // 2
#
#     if start == end:
#         return profits[start]
#
#     return max(sublist_max(profits, start, mid), sublist_max(profits, mid + 1, end),
#                max_crossing_sum(profits, start, end))


# 3번 문제 지금은 스킵
def sublist_max(profits):
    max_profit_so_far = max(max_profit_so_far, max_check)




# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))