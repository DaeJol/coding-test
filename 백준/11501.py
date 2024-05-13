# https://www.acmicpc.net/problem/11501

import sys
imput = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    li = list(map(int, input().rstrip().split()))

    mx = [0 for _ in range(N + 1)]
    currMx = 0
    sum = 0
    for idx, value in enumerate(li[::-1]):
        # print(idx, value)
        currMx = max(value, currMx)
        mx[idx] = currMx
    
    mx.reverse()
    mx.pop(0)
    
    for n in range(N):
        sum += mx[n] - li[n]

    print(sum)
