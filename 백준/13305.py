# 4
# 2 3 1
# 5 2 4 1
N = int(input())
road = list(map(int, input().split(' ')))
price = list(map(int, input().split(' ')))

mn = price[0]
result = price[0] * road[0]
for idx in range(1, N - 1):
    mn = min(price[idx], mn)
    result += mn * road[idx]

print(result)