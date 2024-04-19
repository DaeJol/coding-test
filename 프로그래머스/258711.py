N = int(input())
towers = list(map(int, input().split(' ')))
dp = [0 for _ in range(N)]

for idx, tower in enumerate(towers):
    # print(towers[idx + 1 :])
    for idx2, tower2 in enumerate(towers[idx + 1:], idx + 1):
        
        if tower > tower2: 
            dp[idx2] = idx + 1
        # print(idx2, tower, tower2, towers[idx + 1 : ], dp)

print(' '.join(str(ele) for ele in dp))