a, b, c = 0, 0 ,0

max_num = 21
arr = [[[0 for i in range(max_num)] for j in range(max_num)] for k in range(max_num)]

def rec(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        if arr[20][20][20]:
            return arr[20][20][20]
        else:
            num = rec(20, 20, 20)
            arr[20][20][20] = num
            return num
    elif arr[a][b][c]:
        return arr[a][b][c]
    elif a<b and b<c:
        num = rec(a, b, c-1) + rec(a, b-1, c-1) - rec(a, b-1, c)
        arr[a][b][c] = num
        return num
    else:
        num = rec(a-1, b, c) + rec(a-1, b-1, c) + rec(a-1, b, c-1) - rec(a-1, b-1, c-1)
        arr[a][b][c] = num
        return num

while a != -1 or b != -1 or c != -1:
    a, b, c = map(int, input().split())
    if a != -1 or b != -1 or c != -1:
        print("w(%d, %d, %d) = %d" %(a, b ,c, rec(a, b, c)))
