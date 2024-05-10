s = list(input())

zeroCount = s.count('0')
oneCount = s.count('1')

currZeroCount = zeroCount / 2
currOneCount = oneCount / 2

while currOneCount != 0:
    s.remove('1')
    currOneCount -= 1
    # print(s)

s.reverse()

while currZeroCount != 0:
    s.remove('0')
    currZeroCount -= 1
    # print(s)

s.reverse()

print(''.join(s))

