import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []
orders = int(input().rstrip())

for o in range(orders):
    order = input().rstrip().split()
    if order[0] == 'L':
        if left:
            right.append(left.pop())
    elif order[0] == 'D':
        if right:
            left.append(right.pop())
    elif order[0] == 'B':
        if left:
            left.pop()
    if order[0] == 'P':
        left.append(order[1])

    # print(str, left, list(reversed(right)))
print(''.join(left + list(reversed(right))))