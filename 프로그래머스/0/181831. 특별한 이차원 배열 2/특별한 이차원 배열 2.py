def solution(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1):
            if i != j:
                if arr[i][j] == arr[j][i]:
                    result.append(arr[i][j])
                else:
                    return 0

    return 1