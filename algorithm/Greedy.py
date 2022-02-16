# def min_coin_count(value, coin_list):
#     sum = 0
#     coin_list.sort(reverse=True)
#     for i in range(len(coin_list)):
#         k = 0
#         while coin_list[i] * k < value:
#             k += 1
#         value = value - coin_list[i] * (k - 1)
#         sum += max(0, k - 1)
#     return sum


def min_coin_count(value, coin_list):
    sum = 0
    for coin in sorted(coin_list, reverse=True):
        sum += value // coin
        value = value % coin
    return sum


def max_product(card_lists):
    result = 1
    for i in range(len(card_lists)):
        result *= max(card_lists[i])
    return result


def min_fee(pages_to_print):
    sum = 0
    total = 0
    for page in sorted(pages_to_print):
        total += page
        sum += total
    return sum


# # 테스트
# print(min_fee([6, 11, 4, 1]))
# print(min_fee([3, 2, 1]))
# print(min_fee([3, 1, 4, 3, 2]))
# print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))


def course_selection(course_list):
    result = []
    sorted_list = sorted(course_list, key=lambda x: x[1])
    result.append(sorted_list[0])
    for time in sorted_list:
        if time[0] > result[-1][1]:
            result.append(time)
    return result


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))

