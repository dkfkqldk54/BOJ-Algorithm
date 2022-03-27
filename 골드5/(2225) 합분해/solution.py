num, step = map(int,input().split())

num_list = [1] + [0]*num
cal = 0

for i in range(step):
    for j in range(num):
        cal += num_list[j+1]
        cal %= 1000000000
        num_list[j+1] = cal
    cal = 1
    
res = sum(num_list) % 1000000000
print(res)
