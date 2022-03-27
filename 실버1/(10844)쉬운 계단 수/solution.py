stairs = [ [0] * 10 for _ in range(100)]
stairs[0] = [1] * 10

for i in range(1, 100):
    for j in range(10):
        if j == 0:
            stairs[i][j] = stairs[i-1][j+1]
            stairs[i][j] %= 1000000000
        elif j == 9:
            stairs[i][j] = stairs[i-1][j-1]
            stairs[i][j] %= 1000000000
        else:
            stairs[i][j] = stairs[i-1][j-1] + stairs[i-1][j+1]
            stairs[i][j] %= 1000000000
        
num = int(input())
res = 0
for i in range(1, 10):
    res += stairs[num-1][i]

res %= 1000000000
print(res)
