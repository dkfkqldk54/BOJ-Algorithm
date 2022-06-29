n = int(input())
arr = list(map(int, input().split()))
bt = False
point = 0

i = n-1
while i > 0:
    if arr[i] > arr[i-1]:
        point = i-1
        bt = True
        break
    i -= 1
    
if bt == False:
    print(-1)
else:
    j = n-1
    while j > 0:
        if arr[point] < arr[j]:
            arr[point], arr[j] = arr[j], arr[point]
            break
        j -= 1
    
    res1 = arr[:point+1] 
    res2 = arr[point+1:]
    res2.sort()
    res = res1 + res2
    print(' '.join(map(str, res)))
