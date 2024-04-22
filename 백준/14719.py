# # 4 4
# # 3 0 1 4

H, W = list(map(int, input().split(' ')))
pillows = list(map(int, input().split(' ')))

cnt = 0
for idx in range(1, len(pillows) - 1):
    left = max(pillows[ : idx])
    right = max(pillows[idx + 1 :])
    height = min(left, right)
    if height > pillows[idx]:
        cnt += height - pillows[idx]

print(cnt)

# 4 8
# 3 1 2 3 4 1 1 2 1 1 2
