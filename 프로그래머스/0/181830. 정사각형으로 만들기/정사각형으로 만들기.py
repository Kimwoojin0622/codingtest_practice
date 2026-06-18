def solution(arr):
    row, col = len(arr), len(arr[0])
    
    # step 1. 행의 수가 더 많은 경우 , 행 - 열의 값을 구한 뒤, 각 행 뒤에 행 - 열 값만큼 0을 붙인다.
    if row > col:
        result = []
        diff = row - col
        for i in range(row):
            temp = arr[i]
            for j in range(diff):
                temp.append(0)
            result.append(temp)
    # step 2. 열의 수가 더 많은 경우, 열의 길이만큼 리스트에 [0] * 열길이 추가
    elif col > row:
        result = arr.copy()
        for i in range(col):
            if i > row - 1:
                result.append([0] * col)
        return result
    # step 3. 둘의 길이가 같다면 원래 arr return
    else:
        return arr
        
            
    return result