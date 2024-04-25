# 7
# 3
# 1
# 1
# 5
# 5
# 4
# 6


result = []
N = int(input())
li = [0 for _ in range(N)]


def search(subList, start, end):
    global result
    global N
    global li

    check = True
    selectList = {}
    for select in subList:
        if select < start or select > end:
            check = False
            break
        else:
            selectList[select] = True

    if end - start != len(subList):
        check = False

    # for select in selectList.keys():
    #     if select not in subList:
    #         check = False
    #         break

    if check:
        if len(result) < len(selectList):
            result = selectList.copy()

        print(start, end, selectList, subList)

    temp = []
    for next in range(end + 1, N + 1):
        temp.append(li[next - 1])
        print(subList + temp)
        search(subList + temp, start, next)

for i in range(N):
    li[i] = int(input())

for idx in range(N):
    search([li[idx]], idx + 1, idx + 1)  

print(result)
# resultList = result.keys()
# print(len(resultList))
# for ele in resultList:
#     print(ele)
