turn = int(input())

num_list = list(int(input()) for _ in range(turn))
max_num = max(num_list)

plus_list = [1, 2, 4]
for i in range(2, max_num-1):
  res = plus_list[i] + plus_list[i-1] + plus_list[i-2]
  res %= 1000000009
  plus_list.append(res)

def plus(num, plus_list):
      return plus_list[num-1]
 
for i in num_list:
    num = i
    print(plus(i, plus_list))
