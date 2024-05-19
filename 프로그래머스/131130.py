def solution(cards):
    answer = 0
    group1 = {}
    group2 = {}
    for card in cards:
        currCardIndex = card

        while currCardIndex not in group1:
            group1[currCardIndex] = True
            currCardIndex = cards[currCardIndex - 1]


    return answer