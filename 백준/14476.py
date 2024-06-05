# https://www.acmicpc.net/problem/14476
# https://velog.io/@hyez_dev/%EB%B0%B1%EC%A4%80-14476-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98-%ED%95%98%EB%82%98-%EB%B9%BC%EA%B8%B0-C

import math

def gcd(p,q):
    if p % q == 0:
        return q
    return gcd(q, p % q)

n = int(input())
numbers = list(map(int, input().split()))

ltor = []
rtol = []

ltor.append(numbers[0])
rtol.append(numbers[-1])
for idx in range(1, len(numbers)):
    ltor.append(gcd(ltor[idx - 1], numbers[idx]))
    rtol.append(gcd(rtol[idx - 1], numbers[n - idx - 1]))

rtol.reverse()

result = -1
resultTarget = -1
for i in range(n):
    if i == 0:
        if result < rtol[1]:
            result = rtol[1]
            resultTarget = numbers[0]
    elif i == n - 1:
        if result < ltor[n - 2]:
            result = ltor[n - 2]
            resultTarget = numbers[n - 1]
    else:
        g = gcd(ltor[i - 1], rtol[i + 1])
        if result < g:
            result = g
            resultTarget = numbers[i]

if resultTarget % result == 0:
    print(-1)
else:
    print(result, resultTarget)


