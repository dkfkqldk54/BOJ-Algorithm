m, n = map(int, input().split())
arr = list(input().split())
arr.sort()

abc = ['a', 'e', 'i', 'o', 'u']


permutation = []
visited = [False for _ in range(n)]

def rec(start, depth):
  if depth == m:
    vowel = 0
    consonant = 0
    for c in permutation:
      if c in abc:
        vowel += 1
      else:
        consonant += 1
    if vowel >= 1 and consonant >= 2:
      print(''.join(map(str, permutation)))
    return
  for i in range(start, n):
    if visited[i] == False:
      visited[i] = True
      permutation.append(arr[i])
      rec(i+1, depth+1)
      permutation.pop()
      visited[i] = False

rec(0, 0)
