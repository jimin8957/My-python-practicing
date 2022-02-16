def binary_search(element, some_list):
    s = 0
    e = len(some_list) - 1
    while 1:
        if element == some_list[(s + e) // 2]:
            return ((s + e) // 2)
        elif element not in some_list:
            return None
        elif element > some_list[(s + e) // 2]:
            s = ((s + e) // 2) + 1
        elif element < some_list[(s + e) // 2]:
            e = ((s + e) // 2) - 1




print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))