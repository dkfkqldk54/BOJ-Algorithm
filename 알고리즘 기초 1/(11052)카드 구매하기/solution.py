num = int(input())

cost_char = list(input().split())
cost = []

res = 0

for i in range(num):
    cost.append(int(cost_char[i])/(i+1))


print(cost)
