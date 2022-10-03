def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  left = 0
  right = len(arr)-1
  mid = (left+right)//2
  return merge(mergeSort(arr[left:mid+1]), mergeSort(arr[mid+1:]))

def merge(a, b):
  global cnt
  a1, b1 = len(a), len(b)
  i, j = 0, 0
  tmp = []
  while i < a1 and j < b1:
    if a[i] <= b[j]:
      tmp.append(a[i]); i+=1
    else:
      tmp.append(b[j]); j+=1; cnt += (a1-i)
  if i == a1:
    tmp.extend(b[j:])
  else:
    tmp.extend(a[i:])
  return tmp

cnt = 0
n = int(input())
arr = list(map(int, input().split()))
mergeSort(arr)
print(cnt)
