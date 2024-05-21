# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def dfs(idx, length, curr, result, chars):
    if idx == length:
        result.append(''.join(curr))
        return

    for char in chars:
        curr.append(char)
        dfs(idx + 1, length, curr, result, chars)
        curr.pop()


def solution(word):
    result = []
    chars = ['A', 'E', 'I', 'O', 'U']

    for i in range(1, 6):
        dfs(0, i, [], result, chars)

    result = sorted(result)
    # print(result)
    
    return result.index(word) + 1