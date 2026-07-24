def solution(array, commands):
    result = []
    # step 1. for문으로 commands를 돈다
    for i, j, k in commands:
        
        # step 2. array에서 i-1 부터 ~ j까지 돌고, 정렬을 한다.
        tmp = array[i-1 : j]
        tmp.sort() # O(n log n)
    
        # step 3. 정렬 한 값에서 k-1 값을 result에 append 한다.
        result.append(tmp[k-1])
        
    return result