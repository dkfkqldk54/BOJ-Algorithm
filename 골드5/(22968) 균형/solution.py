fib_arr = [1, 1]

def fib(n):
  if n < len(fib_arr):
    return fib_arr[n]
  else:
    num = fib(n-1) + fib(n-2)
    fib_arr.append(num)
    return num

fib(50)

height_arr = [0, 1]

for i in range(1, len(fib_arr)):
  num = fib_arr[i] + height_arr[i]
  height_arr.append(num)

n = int(input())
for _ in range(n):
  num = int(input())
  i = 0
  while height_arr[i] <= num:
    i += 1
  print(i-1)
