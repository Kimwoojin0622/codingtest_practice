def solution(A, B):
    li, cnt, result = [s for s in A], 0, 0
    for _ in range(len(li) - 1):
        tmp = [0] * len(li)
        for i in range(len(li)):
            if i + 1 > len(li) - 1:
                tmp[0] = li[i]
            elif i + 1 <= len(li) - 1:
                tmp[i + 1] = li[i]
        li = tmp
        cnt += 1
        # print("".join(tmp))
        if "".join(tmp) == B:
            result = cnt
            break
    
    if result > 0:
        if A == B:
            return 0
        else:
            return result
    elif result == 0:
        if A == B:
            return 0
        else:
            return -1
        
        



        