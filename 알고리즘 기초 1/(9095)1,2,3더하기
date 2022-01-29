turn = int(input())

def plus(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        plus_list = [1, 2, 4]
        
        for i in range(2, num-1):
            res = plus_list[i] + plus_list[i-1] + plus_list[i-2]
            plus_list.append(res)
            
        return res
    
for i in range(turn):
    num = int(input())
    print(plus(num))
