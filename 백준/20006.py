p, m = list(map(int, input().split()))

roomList = []
for i in range(p):
    player = list(map(str, input().split()))
    level = int(player[0])

    enter = False
    for room in roomList:
        if room[0] >= level - 10 and room[0] <= level + 10 and len(room[1]) < m:
            room[1].append(player)
            enter = True

            break
    
    if not enter:
        roomList.append([level, [player]])

for room in roomList:
    room[1].sort(key = lambda x: x[1])

    if len(room[1]) == m:
        print('Started!')
    else:
        print('Waiting!')

    for playerInRoom in room[1]:
        print(playerInRoom[0], playerInRoom[1])

    
