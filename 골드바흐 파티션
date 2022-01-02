import sys
input = sys.stdin.readline

turn = int(input())
nums = [int(input()) for i in range(turn)]
m = max(nums)

decimal_list = [False] * 2 +  [True] * (m-1)

for i in range(2, int(m**0.5)+1):
    if decimal_list[i]:
        for j in range(2*i, m+1, i):
            decimal_list[j] = False

for num in nums:
    res = 0

    for i in range(num//2 + 1):
        if decimal_list[i] and decimal_list[num-i]:
                res += 1
            
    print(res)
