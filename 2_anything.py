def exchange(N):
    count = 0
    count += N//500
    N = N%500
    count += N//100
    N = N%100
    count += N//50
    N = N%50
    count += N//10

    return count

print(exchange(1260))