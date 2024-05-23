# 4
# 2 => 0,0 ~ 2,2
# 4
# 5
# 231
def gcd(i, j):
    if j == 0:
        return i
    return gcd(j, i % j)

countList = [0 for _ in range(1001)]
countList[1] = 3
for y in range(2, 1001):
    cnt = 0
    for x in range(1, y + 1):
        if y == x:
            continue

        if gcd(y, x) == 1:
            cnt += 2
    
    countList[y] = countList[y - 1] + cnt 

C = int(input())
for i in range(C):
    N = int(input())
    print(countList[N])