# 6 8  5 3  5 2  6 4
# 5 6  0 0

# [백준] 트리인가?
# https://www.acmicpc.net/problem/6416

class Node:
    def __init__(self, value, vlist, ulist):
        self.value = value
        self.vlist = vlist
        self.ulist = ulist    

k = 1
expectRootNodeList = {}
nodeValueList = {}
edge = 0
isTree = True
isDone = False



while True:
    if isDone:
        break

    pair = input().split("  ")

    for node in pair:
        n = node.split()
        if len(n) < 2:
            continue

        u = int(n[0])
        v = int(n[1])

        if u < 0 and v < 0:
            isDone = True
            break

        if u == 0 and v == 0:
            if len(nodeValueList) == 0 or (isTree and len(expectRootNodeList) == 1 and edge + 1 == len(nodeValueList)):
                print('Case %s is a tree.' % k)
            else:
                print('Case %s is not a tree.' % k)

            k += 1

            # print(n, list(nodeValueList), list(expectRootNodeList))
            expectRootNodeList.clear()
            nodeValueList.clear()
            isTree = True
            edge = 0
            break

        if u == v:
            isTree = False

        # 6
        if u not in nodeValueList:
            nodeValueList[u] = Node(u, [], [])
            expectRootNodeList[u] = True

        # 8
        if v not in nodeValueList:
            nodeValueList[v] = Node(v, [], [])

        edge += 1
        # 6의 자식에 8을 연결
        if v not in nodeValueList[u].vlist:
            nodeValueList[u].vlist.append(v)

        # 8의 부모에 6을 연결
        if u not in nodeValueList[v].ulist:
            nodeValueList[v].ulist.append(u)


        # 부모가 여러개인 순간이 오면 트리가 아님
        if len(nodeValueList[v].ulist) >= 1:
            if len(nodeValueList[v].ulist) > 1:
                isTree = False
            else:
                if v in expectRootNodeList:
                    expectRootNodeList.pop(v)

        # print(n, list(nodeValueList), list(expectRootNodeList))
