# def consecutive_sum(start, end):
#     if end == 2:
#         return 1
#     else:
#         consecutive_sum(start, end - 1)

def consecutive_sum(start, end):
    if end == start:
        return start
    mid = (start + end) // 2
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)


def merge(list1, list2):
    merge_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1
    while i < len(list1) or j < len(list2):
        if i < len(list1):
            merge_list.append(list1[i])
            i += 1
        elif j < len(list2):
            merge_list.append(list2[j])
            j += 1
    return merge_list


def merge_sort(list):
    mid = len(list) // 2
    if len(list) <= 1:
        return list
    return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))



# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    i, b = start, start
    p = my_list[end]
    while i < len(my_list) - 1:
        if my_list[i] > p:
            i += 1
        else:
            swap_elements(my_list, b, i)
            b += 1
            i += 1
    swap_elements(my_list, b, end)
    return b
    # return my_list[:b] + [my_list[end]] + my_list[b - 1:end - 1]


# 퀵 정렬
def quicksort(my_list, start, end):
    if end - start < 1:
        return
    pivot = partition(my_list, start, end)
    quicksort(my_list, start, pivot - 1)
    quicksort(my_list, pivot + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)