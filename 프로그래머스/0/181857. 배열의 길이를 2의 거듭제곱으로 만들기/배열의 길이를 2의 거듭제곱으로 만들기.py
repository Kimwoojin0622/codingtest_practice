def solution(arr):
    # print(2 ** 10)
    # arr의 길이가 최대 1000이기 때문에, 1000이 넘는 2의 거듭제곱 => 2 ** 10 == 1024까지 돌린다.
    sq_2 = [2**i for i in range(11)] # O(10)
    temp = 0
    for n in sq_2:
        if len(arr) <= n: # O(1)
            temp = n
            break
    
    if temp == len(arr):
        return arr
    else:
        length = temp - len(arr)
        for _ in range(length):
            arr.append(0)
    
    return arr
