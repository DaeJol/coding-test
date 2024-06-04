# 3
# 4 4 1
# https://www.acmicpc.net/problem/2904

# 최대공약수이려면 

# 8 24 9
# 2 2 2    2 2 2 3    3 3
# 2 2 3    2 2 3    2 2 3


# 4 5 6 7 8
# 2 2    5    2 3    1 7     2 2 2


# n개를 모두 곱하고
# 약수를 전부 뽑아서
# 그 약수가 몇개가 있는지 구하고
# 그 약수가 n개 인지 구하고
# 그 약수를 n등분한다면 각 숫자에 얼마만큼 전달해줘야되는지 구하고

# 144면 sqrt(144)까지의 수만 계속 나눠주면 된다. 즉 1 ~ 12로만 쭉 나눠주면된다.
# 

import math


def checkPrime():
    global primeList
    for i in range(2, math.floor(math.sqrt(1000000)) + 1):
        if primeList[i]:
            j = 2
            while i * j <= 1000000:
                primeList[i * j] = False
                j += 1

n = int(input())
li = list(map(int, input().split()))
divMapList = [{} for _ in range(n)]
totalDivMap = {}
primeList = [True for _ in range(1000001)]
primes = []

checkPrime()
for i in range(2, 1000000):
    if primeList[i]:
        primes.append(i)

# 100 -> 2 2 5 5
# 54 -> 2 3 3 3
# 102 -> 2 3 17
# 34 -> 2 17
result = 1
resultCount = 0
for idx, number in enumerate(li):
    for prime in primes:
        if number < prime:
            break
        
        if number % prime == 0:
            divMapList[idx][prime] = 0
            totalDivMap[prime] = totalDivMap.get(prime, 0)
            while number % prime == 0:
                divMapList[idx][prime] += 1
                totalDivMap[prime] += 1
                number /= prime

# 2가 n개 이상되었을 때 각각 다 뿌려줌
for key, value in totalDivMap.items():
    if value >= n:
        # 2가 6개 있고 숫자가 5개 있으면 최소 1개씩 (6 / 5) 은 가지고 있어야 됨 -> 6 // 5
        for divList in divMapList:
            # list에 2가
            # 1개 3개 1개 0개 2개
            # 없거나 적은 애들이 몇개 받아와야되는지만 카운트하면 됨
            if key not in divList:
                resultCount += value // n
            elif key in divList and divList[key] < value // n:
                resultCount += ((value // n) - divList[key])
        result *= key * (value // n)

# print(divMapList)
# print(totalDivMap)

print(result, resultCount)