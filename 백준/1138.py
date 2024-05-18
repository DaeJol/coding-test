# 4
# 2 1 1 0

# https://www.acmicpc.net/problem/1138

def check(currList, li):
    for idx, curr in enumerate(currList):
        currCheck = 0
        for i in range(idx):
            if curr < currList[i]:
                currCheck += 1
        
        if li[curr - 1] != currCheck:
            return False
    
    return True

result = []
def com(currList, visited):
    global N
    global li
    global result

    if len(currList) == N:
        if check(currList, li):
            result = currList.copy()

    for i in range(1, N + 1):
        if visited[i] == False:
            visited[i] = True
            currList.append(i)
            com(currList= currList, visited= visited)
            visited[i] = False
            currList.pop()

N = int(input())
li = list(map(int, input().split()))

com(currList = [], visited = [False for _ in range(N + 1)])
print(' '.join(map(str, result)))