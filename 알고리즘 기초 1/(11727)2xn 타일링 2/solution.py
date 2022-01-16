num = int(input())

def com(a, b):
    res = 1
    for i in range(b):
        res *= a-i
        res /= b-i
    res = int(res)
    return res

def com_squ(a, b):
    res = com(a, b)
    res = res * 2**b
    res = res % 10007
    return res

res = 0
a = num
b = 0

while a >= b:
    res += com_squ(a, b)
    res = res % 10007
    a -= 1
    b += 1

print(res)
