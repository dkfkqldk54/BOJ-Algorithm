n = int(input())
card = [i for i in range(1, n+1)]
point = 0
while len(card) - point>1:
  point += 1 # pop(0)
  card.append(card[point])
  point += 1 # card.append(card.pop(0))
print(card[point])
