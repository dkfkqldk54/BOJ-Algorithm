num = int(input())

cost_char = list(input().split())
cost = []

res = 0

for i in range(num):
    cost.append(int(cost_char[i])/(i+1))
    
while num != 0:
    temp_list = cost[:num]
    max_num = max(temp_list)
    max_index = temp_list.index(max_num)
    res += max_num * (max_index+1)
    num -= max_index+1
    
res = int(res)

print(res)
