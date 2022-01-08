num = int(input())

def tile(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    tile_list = [0, 1, 2]
    
    for i in range(3, n+1):
        num = tile_list[i-1] + tile_list[i-2]
        num = num % 15746
        tile_list.append(num)
    return num

res = tile(num)

print(res)
