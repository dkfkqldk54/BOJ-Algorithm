num = int(input())

def tile(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return 3
    
    tile_list = [1, 3]
    
    for i in range(2, n):
        res = 2 * tile_list[i-2] + tile_list[i-1]
        res = res % 10007
        tile_list.append(res)
    return res

print(tile(num))
