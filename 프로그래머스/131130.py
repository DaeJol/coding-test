def solution(cards):
    groups = []
    visited = [0 for _ in range(len(cards) + 1)]

    for card in cards:
        if visited[card]:
            continue

        currGroup = {}
        groups.append(currGroup)
        currCardIndex = card
        while not visited[currCardIndex]:
            currGroup[currCardIndex] = True
            visited[currCardIndex] = True
            currCardIndex = cards[currCardIndex - 1]

    groups = sorted(groups, key=lambda x: -len(x))
    if len(groups) == 1:
        return 0  

    return len(groups[0]) * len(groups[1])