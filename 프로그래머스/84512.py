# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def dfs(idx, length, curr, result, chars):
    # 목표 자리에 도달하면
    if idx == length:
        # 리스트에 넣은거 string으로 만들고 result에 넣어줌
        result.append(''.join(curr))
        return

    # A, E, I, O, U 각각 붙이고 dfs 탐색 한번 더
    for char in chars:
        curr.append(char)
        dfs(idx + 1, length, curr, result, chars)
        curr.pop()


def solution(word):
    result = []
    chars = ['A', 'E', 'I', 'O', 'U']

    # 한자리부터 5자리까지 전부 탐색
    for i in range(1, 6):
        dfs(0, i, [], result, chars)

    # 전부 만든거 리스트 정렬
    result = sorted(result)
    
    return result.index(word) + 1