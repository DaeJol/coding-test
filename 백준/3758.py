T = int(input())
for t in range(T):
    test = list(map(int, input().split(' ')))
    n = test[0]
    k = test[1]
    t = test[2]
    m = test[3]

    team = {}
    for entries in range(int(m)):
        entry = list(map(int, input().split(' ')))
        # 팀의 문제 풀이 정보가 없으면 하나 만들어 줌
        if entry[0] not in team:
            team[entry[0]] = {}
        
        # 팀 당 문제 번호 당 점수
        team[entry[0]][entry[1]] = max(team[entry[0]].get(entry[1], 0), entry[2])

    questions = {}
    for i in range(1, t + 1):
        questions[i] = {}


    for id, quests in team.items():
        
        questions[i] = []

    print(team)