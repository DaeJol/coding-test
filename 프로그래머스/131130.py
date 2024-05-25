# [프로그래머스] 131130. 혼자 놀기의 달인
# https://school.programmers.co.kr/learn/courses/30/lessons/131130?language=python3

def solution(cards):
    groups = []
    # 상자가 오픈됐는지 저장
    visited = [0 for _ in range(len(cards) + 1)]

    for card in cards:
        # 현재 탐색하려는 상자가 오픈됐다? 무시
        if visited[card]:
            continue

        # 각 그룹을 리스트에 담을 예정임
        currGroup = {}
        groups.append(currGroup)
        currCardIndex = card

        # 현재 탐색 중인 카드를 가진 상자가 오픈됐는지 보고
        while not visited[currCardIndex]:
            # 오픈 안됐으면 오픈시키고 다음 카드 상자 오픈 준비
            currGroup[currCardIndex] = True
            visited[currCardIndex] = True
            currCardIndex = cards[currCardIndex - 1]

    # 단순 내림차순 정렬을 파이썬은 이렇게 표현합니다
    groups = sorted(groups, key=lambda x: -len(x))

    # 그룹이 1개다 = 1번 그룹밖에 없다 = 0점
    if len(groups) == 1:
        return 0  

    return len(groups[0]) * len(groups[1])