future, present = map(int, input().split())
turn = int(input())

numbers = input().split()

decimal = 0

for i in range(turn):
    number = int(numbers[i])
    decimal += number * (future ** (turn - i - 1))

res = []

while decimal != 0:
    rem = decimal % present
    res.append(rem)
    decimal = decimal // present

print(res)
    
for i in range(len(res)):
    print(res.pop(), end=' ')
