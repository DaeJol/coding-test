import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
keywords = {}
for i in range(N):
    keywords[input().rstrip()] = 1

for i in range(M):
    keywordList = list(input().rstrip().split(','))
    for keyword in keywordList:
        keywords.pop(keyword, None)
    print(len(keywords))
