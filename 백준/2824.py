def gcd(a, b):
    while b > 0:
        next = a % b
        a = b
        b = next
    return a

def mul(lst) :
    return eval('*'.join([str(n) for n in lst]))


N = int(input())
nlist = list(map(int, input().split()))

M = int(input())
mlist = list(map(int, input().split()))

a = mul(nlist)
b = mul(mlist)

print('%s' % str(gcd(a, b))[-9:])