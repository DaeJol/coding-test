# https://www.acmicpc.net/problem/14002 

n = int(input())
a = list(map(int, input().split()))
dp = [[a[i]] for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and len(dp[i]) < len(dp[j]) + 1:
            dp[i] = dp[j].copy()
            dp[i].append(a[i])

# print(dp)
result = []
for d in dp:
    if len(d) > len(result):
        result = d

print(len(result))
print(' '.join(list(map(str, result))))
