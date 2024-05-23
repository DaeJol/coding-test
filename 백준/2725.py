# 4
# 2 => 0,0 ~ 2,2
# 4
# 5
# 231

C = int(input())
for i in range(C):
    m = {}
    N = int(input())

    for y in range(1, N + 1):
        for x in range(1, N + 1):
            m[y / x] = True

    print(len(m) + 2)