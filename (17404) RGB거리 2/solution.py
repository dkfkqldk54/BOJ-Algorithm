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

a = min(arr[n-1][1], arr[n-1][2])
b = min(arr[n-1][0], arr[n-1][2])
c = min(arr[n-1][0], arr[n-1][1])
    
arr[0][0] = min(arr[n-1][1], arr[n-1][2]) + arr[0][0]
arr[0][1] = min(arr[n-1][0], arr[n-1][2]) + arr[0][1]
arr[0][2] = min(arr[n-1][0], arr[n-1][1]) + arr[0][2]
    
for i in range(1, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
    
arr[n-1][0] -= a
arr[n-1][1] -= b
arr[n-1][2] -= c

res = min(arr[n-1])

print(res)

여기서 달라진 점은 딱 1개
첫 번째와 마지막은 색이 달라야 한다.

마지막 조합이 나오면 또 색 조합이 다 달라질 거라고
처음부터 dp로 구성해야 한다는 뜻이야

71 39 44(가.로 인해 마지막 줄과 다른 색 선택)
32 83 55
51 37 63
89 29 100
83 58 11
65 13 15
47 25 29(나.로 인해 앞줄과 다른 색 선택)
60 66 19

이렇게 수로 된 띠를 둥글게 말아봐
그럼 처음부터 맨 첫번째는 맨 마지막 수를 신경써서 고르면 되는 거네 !!!

근데 맨 마지막도 그 다음 수를 신경써서 골라야 해
식을 똑같이 만들어주면 어디서 중복이 발생하는가?

60 66 19
71 39 44(가.로 인해 마지막 줄과 다른 색 선택)
32 83 55
51 37 63
89 29 100
83 58 11
65 13 15
47 25 29
60 66 19(나.로 인해 앞줄과 다른 색 선택)

사실상 이렇게 되는 거야

