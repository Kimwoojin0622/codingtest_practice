def solution(num, total):
    result = []
    if total == 0:
        tmp = num // 2
        for i in range(-tmp, tmp + 1):
            result.append(i)
    elif num > total:
        for i in range(-total + 1, total + 1):
            result.append(i)
    elif total >= num:
        is_True, count = True, total
        num_list = [i for i in range(num)]
        while is_True:
            tmp = []
            for i in range(len(num_list)):
                tmp.append(count - num_list[i])
            if sum(tmp) == total:
                is_True = False
            count = count - 1
        
        tmp.sort()
        return tmp
    
    result.sort()
    return result
            