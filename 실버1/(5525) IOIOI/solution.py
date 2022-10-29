n = int(input())
m = int(input())
s = input()

p = 'I'
for _ in range(n):
  p += 'OI'

cnt = 0
num_of_ioi = 0

i = 0
while i <= (m-2):
  if s[i:i+3] == 'IOI':
    num_of_ioi += 1
    i += 2
    if num_of_ioi >= n:
      cnt += 1
  else:
    num_of_ioi = 0
    i += 1

print(cnt)
