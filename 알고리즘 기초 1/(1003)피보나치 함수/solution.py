turn = int(input())

def fib_zero(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    fib_arr = [1, 0]
    
    for i in range(2, n+1):
        num = fib_arr[i-1] + fib_arr[i-2]
        fib_arr.append(num)
    return fib_arr[n]

def fib_one(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_arr = [0, 1]
    
    for i in range(2, n+1):
        num = fib_arr[i-1] + fib_arr[i-2]
        fib_arr.append(num)
    return fib_arr[n]

for i in range(turn):
    num = int(input())
    
    print(fib_zero(num), end=' ')
    print(fib_one(num))
