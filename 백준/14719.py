# 4 4
# 3 0 1 4

H, W = list(map(int, input().split(' ')))
pillows = list(map(int, input().split(' ')))

stack = []
curr = -1
cnt = 0
for pillow in pillows:
    if curr == -1:
        if pillow > 0:
            curr = pillow
    else:
        print(pillow, curr, stack)
        # 현재 기둥이 맨처음의 기준 기둥보다 높거나 같으면 stack에서 전부 빼서 높이 계산해준다.
        if pillow >= curr:
            while stack:
                cnt += (curr - stack.pop())
            curr = -1
        else:
            stack.append(pillow)
        print('cnt: ', cnt)

print(curr, stack)
if stack and stack[-1] > 0:
    s = stack.pop()
    while stack:
        cnt += s - stack.pop()

print(cnt)
