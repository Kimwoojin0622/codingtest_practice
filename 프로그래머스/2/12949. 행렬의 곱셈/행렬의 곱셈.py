def solution(arr1, arr2):
    # O(N^3) 가능
    result = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            num = 0
            for k in range(len(arr2)):
                num += arr1[i][k] * arr2[k][j]
            tmp.append(num)
        result.append(tmp)
    
    return result