N = int(input())

wordMap = {}
word = list(input())
answer = 0

for idx in range(N - 1):
    nWord = list(input())
    tWord = word.copy()
    templist = []
    # 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어
    while tWord:
        w = tWord.pop()
        if w in nWord:
            nWord.remove(w)
        else:
            templist.append(w)

    if max(len(templist), len(nWord)) <= 1:
        answer += 1
        

print(answer)

