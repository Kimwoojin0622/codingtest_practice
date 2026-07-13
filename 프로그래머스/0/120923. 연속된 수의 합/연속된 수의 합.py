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
        num_list, count = [i for i in range(num)], total
        while True:
            tmp = []
            for i in range(len(num_list)):
                tmp.append(count - num_list[i])
            if sum(tmp) == total:
                break
            count = count - 1
            
        tmp.sort() # O(n log n)
        return tmp
    
    return result
