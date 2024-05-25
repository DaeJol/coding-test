# 백준 2824. 최대공약수
# https://www.acmicpc.net/problem/2824

# 유클리드 호제법
# https://namu.wiki/w/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C%20%ED%98%B8%EC%A0%9C%EB%B2%95
def gcd(a, b):
    while b > 0:
        next = a % b
        a = b
        b = next
    return a

def mul(lst) :
    # eval: string 수식을 실제 연산으로 적용해준다.
    # '10*20*30' 이라고 string으로 되어있는 수식을 읽어서 실제 6000의 결과값을 내줌
    return eval('*'.join([str(n) for n in lst]))


N = int(input())
nlist = list(map(int, input().split()))

M = int(input())
mlist = list(map(int, input().split()))

a = mul(nlist)
b = mul(mlist)

print('%s' % str(gcd(a, b))[-9:])