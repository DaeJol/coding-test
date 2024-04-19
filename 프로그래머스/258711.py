N = int(input())
towers = list(map(int, input().split(' ')))
result = [0 for _ in range(N)]
# [인덱스, 높이]
stack = []

# towers.reverse() --> void
# towers = reversed(towers)
# towers = towsers[::-1]
towers.reverse()
for idx in range(len(towers)):
    curr = towers[idx]
    if not stack:
        stack.append([idx, curr])
    else:
        while stack:
            top = stack[-1]
            if top[1] < curr:
                result[top[0]] = len(towers) - idx
                stack.pop()
            else:
                break

        stack.append([idx, curr]) 
    # print('result:', result)

print(' '.join(str(e) for e in reversed(result)))