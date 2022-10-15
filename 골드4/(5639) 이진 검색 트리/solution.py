import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

num_arr = []
while True:
  try:
    num_arr.append(int(input()))
  except:
    break

def postOrder(start, end):
  if start > end:
    return

  mid = end + 1
  for i in range(start+1, end+1):
    if num_arr[start] < num_arr[i]:
      mid = i
      break
  
  postOrder(start+1, mid-1)
  postOrder(mid, end)
  print(num_arr[start])

postOrder(0, len(num_arr)-1)
