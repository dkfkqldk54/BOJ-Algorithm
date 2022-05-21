<원래 코드>
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

<수정 코드>
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
    
arr[n-1][0] -= a
arr[n-1][1] -= b
arr[n-1][2] -= c

res = min(arr[n-1])

print(res)

#0번째 색깔을 기준

arr[2][0] = min(arr[1][1], arr[1][2]) + arr[0][0] + arr[2][0]
arr[2][1] = min(arr[1][1], arr[1][2]) + arr[0][0] + arr[2][1]
arr[2][2] = min(arr[1][1], arr[1][2]) + arr[0][0] + arr[2][2]

for i in range(3, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
    
res = min(arr[i-1][1], arr[i-1][2])

#1번째 색깔을 기준

arr[2][0] = min(arr[1][0], arr[1][2]) + arr[0][1] + arr[2][0]
arr[2][1] = min(arr[1][0], arr[1][2]) + arr[0][1] + arr[2][1]
arr[2][2] = min(arr[1][0], arr[1][2]) + arr[0][1] + arr[2][2]

for i in range(3, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
    
res = min(arr[i-1][0], arr[i-1][2])

#2번째 색깔을 기준

arr[2][0] = min(arr[1][0], arr[1][1]) + arr[0][2] + arr[2][0]
arr[2][1] = min(arr[1][0], arr[1][1]) + arr[0][2] + arr[2][1]
arr[2][2] = min(arr[1][0], arr[1][1]) + arr[0][2] + arr[2][2]

for i in range(3, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
    
res = min(arr[i-1][0], arr[i-1][2])
