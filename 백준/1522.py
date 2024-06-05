# https://www.acmicpc.net/problem/1522
# 양 끝지점이 a이고 나머지 a는 모두 연속하면 됨

# aaaaaaaabbbb
# baaaaaaaabbb
# bbaaaaaaaabb
# bbbaaaaaaaab
# bbbbaaaaaaaa
# abbbbaaaaaaa
# aabbbbaaaaaa
# aaabbbbaaaaa
# aaaabbbbaaaa
# aaaaabbbbaaa
# aaaaaabbbbaa
# aaaaaaabbbba

# b뭉치가 돌아다니는 케이스로

# baaaaaaaabbb
# aabbaaabaaba
# x0xx000x0x0x -> 3번 바꿔야됨

# baaaaaaaabbb
# aaabbbbaaaaa
# x00xxxx00xxx -> 4번 바꿔야됨

str = input()
ac = 0
bc = 0

for s in str:
    if s == 'a':
        ac += 1
    else:
        bc += 1


result = 10000000
for i in range(ac + 1):
    currStr = 'a' * i + 'b' * bc + 'a' * (ac - i)
    # print(currStr)

    currCnt = 0
    for i in range(len(str)):
        if currStr[i] != str[i]:
            currCnt += 1

    result = min(result, currCnt / 2)

for i in range(bc + 1):
    currStr = 'b' * i + 'a' * ac + 'b' * (bc - i)
    # print(currStr)

    currCnt = 0
    for i in range(len(str)):
        if currStr[i] != str[i]:
            currCnt += 1

    result = min(result, currCnt / 2)

print(int(result))
