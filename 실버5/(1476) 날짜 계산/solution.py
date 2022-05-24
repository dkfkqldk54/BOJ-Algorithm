year_cal = [0 for i in range(100001)]

e, s, m = map(int, input().split())

while e < 10000:
  year_cal[e] += 1
  e += 15

while s < 10000:
  year_cal[s] += 1
  s += 28

while m < 10000:
  year_cal[m] += 1
  m += 19

res = year_cal.index(3)
print(res)
