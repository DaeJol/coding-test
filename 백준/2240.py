# # 7 2
# # 2
# # 1
# # 1
# # 2
# # 2
# # 1
# # 1

# T, W = list(map(int, input().split()))

# fn = int(input())

# tree1 = [[] for _ in range(1001)]
# tree2 = [[] for _ in range(1001)]

# if fn == 1:
#     tree1[1].append([1, W])
#     tree2[1].append([0, W - 1])
# else:
#     tree1[1].append([0, W])
#     tree2[1].append([1, W - 1])


# for idx in range(2, T + 1):
#     n = int(input())

#     for t1 in tree1[idx - 1]:
#         if n == 1:
#             tree1[idx].append([t1[0] + 1, t1[1]])
#             tree2[idx] = tree2[idx - 1].copy()
#         else:
#             tree1[idx] = tree1[idx - 1].copy()
#             if t1[1] > 0:
#                 tree2[idx].append([t1[0] + 1, t1[1] - 1])
                

#     for t2 in tree2[idx - 1]:
#         if n == 1:
#             if t2[1] > 0:
#                 tree1[idx].append([t2[0] + 1, t2[1] - 1])
#             tree2[idx] = tree2[idx - 1].copy()
#         else:
#             tree1[idx] = tree1[idx - 1].copy()
#             tree2[idx].append([t2[0] + 1, t2[1]])

#     # print('n:::::::::::::::::::::::::::::',idx, n,'::::::::::::::::::::::::::::')
#     # print("tree1----------------------------------")

#     # for i in range(T + 1):
#     #     print('i:',i,' ', tree1[i])

#     # print("tree2----------------------------------")


#     # for i in range(T + 1):
#     #     print('i:',i,' ', tree2[i])
    
#     # print("-----")

# result = 0
# for t1 in tree1[T]:
#     result = max(t1[0], result)

# for t2 in tree2[T]:
#     result = max(t2[0], result)

# print(result)

