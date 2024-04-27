import sys
input = sys.stdin.readline

N = int(input())
cons = [0 for _ in range(1600000)]
val = [0 for _ in range(1600000)]
dp = [0 for _ in range(1600000)]

for i in range(1, N + 1):
    cost, value = list(map(int, input().split(' ')))
    dp[i] = max(dp[i - 1], dp[i])
    if i + cost - 1 <= N:
        dp[i + cost - 1] = max(value + dp[i - 1], dp[i + cost - 1])


print(max(dp))