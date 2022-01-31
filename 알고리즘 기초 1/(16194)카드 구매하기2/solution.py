num = int(input())
card = [0] + list(map(int, input().split()))
min_list = [0] * (num + 1)

min_list[1] = card[1]
min_list[2] = min(card[1] * 2, card[2])

for i in range(3, num+1):
    min_list[i] = card[i]
    for j in range(1, i//2 + 1):
        min_list[i] = min(min_list[i], min_list[j] + min_list[i-j])
        
print(min_list[num])
