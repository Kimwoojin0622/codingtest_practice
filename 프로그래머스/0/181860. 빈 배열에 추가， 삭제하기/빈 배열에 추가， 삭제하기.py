def solution(arr, flag):
    X = []
    for i in range(len(arr)):
        if flag[i]:
            length = arr[i] * 2
            for _ in range(length):
                X.append(arr[i])
            # print(X)
        else:
            length = arr[i]
            for _ in range(length):
                X.pop()
            # print(X)
    return X
