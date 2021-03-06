# N이 홀수일 때는 경우의 수가 0이다.
# 3X2 타일을 채우는 경우의 수는 3개이다.
# 3X2 타일을 활용하지 않고 3X4 타일을 채우는 경우의 수는 2개이다.
# 이전 타일을 활용하지 않고 3XM(M은 4이상의 짝수) 타일을 채우는 경우의 수는 2개다.

# N을 N이하의 자연수 짝수의 합으로 표현하는 방법은 다음과 같다.
# N=2일 때: 2
# N=4일 때: 2+2 = 4
# N=6일 때: 2+2+2 = 2+4 = 4+2 = 6
# N일 때 경우의 수는 N, N-2일 때 경우의 수에서 2을 더한 것, N-4일 때 경우의 수에서 4를 더한 것, ... , 2일 때 경우의 수에서 N-2를 더한 것으로 구성된다.

# 여기서 2를 3X2 타일을 채우는 경우의 수, 4를 3X2 타일을 활용하지 않고 3X4 타일을 채우는 경우의 수, ... 라고 생각하면 3XN 타일을 채우는 경우의 수는 아래와 같이 분해할 수 있다.
# 3X2 경우의 수 분해: 3X2 경우의 수
# 3X4 경우의 수 분해: 3X2 경우의 수 * 3X2 경우의 수 + 3X4에서만 가능한 경우의 수
# 3X6 경우의 수 분해: 3X2 경우의 수 * 3X2 경우의 수 * 3X2 경우의 수 + 3X2 경우의 수 * 3X4에서만 가능한 경우의 수 + 3X4에서만 가능한 경우의 수 * 3X2 경우의 수 + 3X6에서만 가능한 경우의 수
# 따라서 3XN 경우의 수를 DP[N]이라고 가정하면, DP[N] = DP[N-1]*3 + DP[N-2] * 2 + DP[N-3] * 2 + ... + DP[1] * 2 + 2로 일반화시킬 수 있다. 

n = int(input())
dp = [0 for i in range(31)]
dp[2] = 3

if n >= 4:
  for i in range(4, n+1, 2):
    for j in range(i):
        dp[i] += dp[j] * 2
    dp[i] += dp[i-2] + 2
        
print(dp[n])
