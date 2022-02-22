import math

num = int(input())
dp = [1] * (num + 1)

for i in range(num+1):
    dp[i] = i
    for j in range(1, int(math.sqrt(i))+1):
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1
            
print(dp[num])
