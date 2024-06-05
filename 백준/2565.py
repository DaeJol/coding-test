# 8
# 1 8 -> 1-8: [2-2, 4-1, ...] y = -7/2x + 1
# 3 9
# 2 2
# 4 1
# 6 4
# 10 10
# 9 7
# 7 6

# 한 선의 start end가 다른 선의 start end보다 둘 다 크거나 둘 다 작으면 안 겹침

#################
# 아래 풀이 생각해보면
# 짧은거 지웠는데 우연찮게 핵심인 겹치는 줄 몇개 사라져서 한꺼번에 통으로 사라지게끔 할 수도 있어서
# 가장 겹치는게 많은 순으로 지운다고 해결되는 문제는 아니다.
# links = {}

# n = int(input())
# for i in range(n):
#     link = input()
#     links[link] = []

# for link in links.keys():
#     for key, value in links.items():
#         curr = list(map(int, link.split()))
#         target = list(map(int, key.split()))

#         if curr[0] == target[0] and curr[1] == target[1]:
#             continue

#         if key in links[link]:
#             continue

#         if (curr[0] <= target[0] and curr[1] <= target[1]) or (curr[0] >= target[0] and curr[1] >= target[1]):
#             continue


#         links[link].append(key)
#         links[key].append(link)

# links = dict(sorted(links.items(), key=lambda x: len(x[1]), reverse=True))
# cnt = 0
# print(links)
# for key, value in links.items():
#     if len(value) > 0:
#         cnt += 1
#         for val in value:
#             links[val].remove(key)
        

# print(cnt)



# 가장 긴 증가하는 부분수열과 같은 유형
n = int(input())
dp = [1 for _ in range(n)]
links = []
for i in range(n):
    links.append(input())

links = sorted(links, key=lambda x: list(map(int, x.split()))[0])

dp[0] = 1
result = 0
for i, link in enumerate(links):
    for j in range(i):
        link1 = list(map(int, link.split()))
        link2 = list(map(int, links[j].split()))
        if (link1[0] <= link2[0] and link1[1] <= link2[1]) or (link1[0] >= link2[0] and link1[1] >= link2[1]):
            dp[i] = max(dp[j] + 1, dp[i])

for d in dp:
    result = max(result, d)

print(n - result)
