def solution(arr):
    cnt = 0
    while True:
        result = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                result.append(i / 2)
            elif i < 50 and i % 2 != 0:
                result.append(i * 2 + 1)
            else:
                result.append(i)
        if arr == result:
            return cnt
        
        arr = result
        cnt += 1
    return cnt