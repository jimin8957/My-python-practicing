def fib_memo(n, cache):
    if n == 1 or n == 2:
        return 1
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)

def fib_tab(n):
    list = [0, 1, 1]
    for i in range(3, n + 1):
        list.append(list[i - 1] + list[i - 2])
    return list[n]


def fib_optimized(n):
    pre = 0
    current = 1
    k = 0
    while k < n - 1:
        temp = pre
        pre = current
        current = temp + current
        k += 1
    return current


def max_profit_memo(price_list, count, cache):
    if count <= 1:
        cache[count] = price_list[count]
        return cache[count]
    if count in cache:
        return cache[count]
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0
    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))
    cache[count] = profit
    return profit

def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


def max_profit_tab(price_list, count):
    profit_table = [0]
    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_tab(price_list, i) + max_profit_tab(price_list, count - i))


# 테스트
print(max_profit_tab([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit_tab([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit_tab([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
