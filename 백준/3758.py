T = int(input())
for t in range(T):
    test = list(map(int, input().split(' ')))
    n = test[0] # 팀 개수
    k = test[1] # 문제 개수
    t = test[2] # 우리팀의 id
    m = test[3] # 문제 수

    # id, 문제 번호, 점수
    # 1 1 30
    # 2 3 30
    # 1 2 40
    # 1 2 20
    # 3 1 70

    # 1번: [[id, 30점, 제출 횟수, 제출 시간], [], []]
    # 2번: []
    # questions[문제 번호][문제 개수][팀 번호]
    # 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다. 
    # 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높다. 

    # 1팀: [점수, 제출 횟수, 제출 시간]
    teams = [[0 for _ in range(5)] for _ in range(n + 1)]
    teamQuestions = {}
    for entryIndex in range(int(m)):
        entry = list(map(int, input().split(' ')))
        id = entry[0]
        no = entry[1]
        score = entry[2]

        if id not in teamQuestions:
            teamQuestions[id] = [0 for _ in range(k + 1)]        
        # 초기화가 안됐으면 빈 dict 만들어준다.
        teams[id][0] = id
        teamQuestions[id][no] = max(teamQuestions[id][no], score)
        teams[id][2] += 1 
        teams[id][3] = entryIndex

    for teamId, questions in teamQuestions.items():
        teams[teamId][1] = sum(questions)

    teams.sort(key = lambda x: (x[1], -x[2], -x[3]), reverse=True)
        
    # print(teams)

    rank = 1
    for team in teams:
        if team[0] == 0:
            continue

        if team[0] != t:
            rank += 1
        else:
            break

    print(rank)
    
    

