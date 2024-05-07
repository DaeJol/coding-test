import sys
input = sys.stdin.readline

N, M = list(map(int, input().split(' ')))
typeList = []
for t in range(N):
    type, amount = list(map(str, input().split(' ')))
    typeList.append([type, int(amount)])
typeList.sort(key=lambda x: x[1])

for n in range(M):
    a = int(input().rstrip())

    start = 0
    end = len(typeList)
    mid = -1
    result = ''
    while start <= end:
        mid = (start + end) // 2

        if typeList[mid][1] >= a: 
             end = mid - 1
             result = typeList[mid][0]
        elif typeList[mid][1] < a:
            start = mid + 1
    print(result)