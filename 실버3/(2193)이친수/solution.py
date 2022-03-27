n = int(input())

def pinary(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        pinary_list = [1, 1]
        
        for i in range(2, num):
            res = pinary_list[i-2] + pinary_list[i-1]
            pinary_list.append(res)
        return res

print(pinary(n))
