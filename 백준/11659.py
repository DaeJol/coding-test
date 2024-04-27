import sys
input = sys.stdin.readline

N, M = list(map(int, input().split(' ')))
numbers = list(map(int, input().split(' ')))
dp = [0 for _ in range(N + 1)]
dp[0] = 0

for idx, number in enumerate(numbers):
    dp[idx + 1] = dp[idx] + number

for n in range(M):
    start, end = list(map(int, input().split(' ')))
    print(dp[end] - dp[start - 1])