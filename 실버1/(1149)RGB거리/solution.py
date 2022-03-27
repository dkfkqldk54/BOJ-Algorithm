turn = int(input())
num_list = []
for i in range(turn):
    num_list.append(list(map(int, input().split())))
for i in range(1, turn):
    num_list[i][0] = min(num_list[i-1][1], num_list[i-1][2]) + num_list[i][0]
    num_list[i][1] = min(num_list[i-1][0], num_list[i-1][2]) + num_list[i][1]
    num_list[i][2] = min(num_list[i-1][0], num_list[i-1][1]) + num_list[i][2]
res = min(num_list[turn-1])
print(res)
